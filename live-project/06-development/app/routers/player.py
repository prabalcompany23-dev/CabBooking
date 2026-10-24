from datetime import datetime

from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.config import Settings, get_settings
from app.db import get_db
from app.models.venue_booking import VenueBooking
from app.services.pilot import is_pilot_eligible
from app.services.ride_requests import create_ride_request

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


def _parse_game_time(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail="Invalid game date/time.") from exc


def _guest_display_name(mobile: str) -> str:
    digits = "".join(ch for ch in mobile if ch.isdigit())
    suffix = digits[-4:] if len(digits) >= 4 else digits or "????"
    return f"Guest · {suffix}"


def _save_venue_booking(
    db: Session,
    *,
    player_name: str,
    contact: str,
    city: str,
    sport: str,
    venue_name: str,
    game_starts_at: str,
    own_vehicle: bool,
) -> VenueBooking:
    contact_val = contact.strip()
    if not contact_val or len(contact_val) > 80:
        raise HTTPException(status_code=400, detail="Contact is required.")
    city_val = city.strip()
    sport_val = sport.strip()
    venue = venue_name.strip()
    if not city_val or not sport_val or not venue:
        raise HTTPException(status_code=400, detail="City, sport, and venue are required.")
    name = player_name.strip()
    if not name or len(name) > 120:
        raise HTTPException(status_code=400, detail="Player name is required.")

    booking = VenueBooking(
        player_name=name,
        contact=contact_val,
        city=city_val,
        sport=sport_val,
        venue_name=venue,
        game_starts_at=_parse_game_time(game_starts_at),
        own_vehicle=own_vehicle,
    )
    db.add(booking)
    db.commit()
    db.refresh(booking)
    return booking


@router.get("/", response_class=HTMLResponse)
def book_venue_form(request: Request, settings: Settings = Depends(get_settings)) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "book.html",
        {
            "pilot_city": settings.pilot_city,
            "pilot_sport": settings.pilot_sport,
            "error": None,
        },
    )


@router.post("/")
def book_venue_submit(
    player_name: str = Form(...),
    contact: str = Form(...),
    city: str = Form(...),
    sport: str = Form(...),
    venue_name: str = Form(...),
    game_starts_at: str = Form(...),
    own_vehicle: str | None = Form(None),
    db: Session = Depends(get_db),
) -> RedirectResponse:
    booking = _save_venue_booking(
        db,
        player_name=player_name,
        contact=contact,
        city=city,
        sport=sport,
        venue_name=venue_name,
        game_starts_at=game_starts_at,
        own_vehicle=own_vehicle == "on",
    )
    return RedirectResponse(url=f"/bookings/{booking.id}", status_code=303)


@router.get("/guest", response_class=HTMLResponse)
def guest_book_form(request: Request, settings: Settings = Depends(get_settings)) -> HTMLResponse:
    return templates.TemplateResponse(
        request,
        "guest_book.html",
        {
            "pilot_city": settings.pilot_city,
            "pilot_sport": settings.pilot_sport,
        },
    )


@router.post("/guest")
def guest_book_submit(
    mobile: str = Form(...),
    city: str = Form(...),
    sport: str = Form(...),
    venue_name: str = Form(...),
    game_starts_at: str = Form(...),
    own_vehicle: str | None = Form(None),
    db: Session = Depends(get_db),
) -> RedirectResponse:
    mobile_val = mobile.strip()
    if not mobile_val or len(mobile_val) > 80:
        raise HTTPException(status_code=400, detail="Mobile number is required.")
    booking = _save_venue_booking(
        db,
        player_name=_guest_display_name(mobile_val),
        contact=mobile_val,
        city=city,
        sport=sport,
        venue_name=venue_name,
        game_starts_at=game_starts_at,
        own_vehicle=own_vehicle == "on",
    )
    return RedirectResponse(url=f"/bookings/{booking.id}", status_code=303)


@router.get("/bookings/{booking_id}", response_class=HTMLResponse)
def booking_confirm(
    request: Request,
    booking_id: int,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> HTMLResponse:
    booking = db.get(VenueBooking, booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found.")
    eligible = is_pilot_eligible(booking.city, booking.sport, booking.own_vehicle, settings)
    return templates.TemplateResponse(
        request,
        "booking_confirm.html",
        {"booking": booking, "ride_eligible": eligible},
    )


@router.get("/bookings/{booking_id}/ride/new", response_class=HTMLResponse)
def ride_form(
    request: Request,
    booking_id: int,
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> HTMLResponse:
    booking = db.get(VenueBooking, booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found.")
    if not is_pilot_eligible(booking.city, booking.sport, booking.own_vehicle, settings):
        raise HTTPException(status_code=400, detail="Ride request not available for this booking.")
    return templates.TemplateResponse(
        request,
        "ride_form.html",
        {"booking": booking, "error": None},
    )


@router.post("/bookings/{booking_id}/ride/new")
def ride_submit(
    booking_id: int,
    pickup_area: str = Form(...),
    db: Session = Depends(get_db),
    settings: Settings = Depends(get_settings),
) -> RedirectResponse:
    booking = db.get(VenueBooking, booking_id)
    if booking is None:
        raise HTTPException(status_code=404, detail="Booking not found.")
    if not is_pilot_eligible(booking.city, booking.sport, booking.own_vehicle, settings):
        raise HTTPException(status_code=400, detail="Ride request not available for this booking.")
    pickup = pickup_area.strip()
    if not pickup or len(pickup) > 200:
        raise HTTPException(status_code=400, detail="Pickup area is required.")
    ride = create_ride_request(db, booking, pickup)
    return RedirectResponse(url=f"/ride-requests/{ride.id}/confirmed", status_code=303)


@router.get("/ride-requests/{ride_id}/confirmed", response_class=HTMLResponse)
def ride_confirmed(request: Request, ride_id: int, db: Session = Depends(get_db)) -> HTMLResponse:
    from app.models.ride_request import RideRequest

    ride = db.get(RideRequest, ride_id)
    if ride is None:
        raise HTTPException(status_code=404, detail="Ride request not found.")
    return templates.TemplateResponse(
        request,
        "ride_confirmed.html",
        {"ride": ride, "booking": ride.venue_booking},
    )
