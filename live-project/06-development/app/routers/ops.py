from fastapi import APIRouter, Depends, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, joinedload

from app.db import get_db
from app.models.ride_request import RideRequest, RideRequestStatus
from app.services.auth import authenticate_ops
from app.services.ride_requests import update_ride_status

router = APIRouter(prefix="/ops")
templates = Jinja2Templates(directory="app/templates")


def require_ops_session(request: Request) -> None:
    if not request.session.get("ops_authenticated"):
        raise HTTPException(status_code=401, detail="Ops login required")


@router.get("/login", response_class=HTMLResponse)
def ops_login_form(request: Request, error: int | None = None) -> HTMLResponse:
    message = "Invalid username or password." if error else None
    return templates.TemplateResponse(request, "ops/login.html", {"error": message})


@router.post("/login")
def ops_login_submit(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db),
) -> RedirectResponse:
    if not authenticate_ops(db, username.strip(), password):
        return RedirectResponse(url="/ops/login?error=1", status_code=303)
    request.session["ops_authenticated"] = True
    request.session["ops_username"] = username.strip()
    return RedirectResponse(url="/ops/queue", status_code=303)


@router.post("/logout")
def ops_logout(request: Request) -> RedirectResponse:
    request.session.clear()
    return RedirectResponse(url="/ops/login", status_code=303)


def _ops_session(request: Request) -> None:
    require_ops_session(request)


@router.get("/queue", response_class=HTMLResponse)
def ops_queue(
    request: Request,
    db: Session = Depends(get_db),
    _: Annotated[None, Depends(_ops_session)] = None,
) -> HTMLResponse:
    rides = (
        db.query(RideRequest)
        .options(joinedload(RideRequest.venue_booking))
        .order_by(RideRequest.created_at.desc())
        .all()
    )
    return templates.TemplateResponse(
        request,
        "ops/queue.html",
        {"rides": rides, "username": request.session.get("ops_username")},
    )


@router.get("/requests/{ride_id}", response_class=HTMLResponse)
def ops_request_detail(
    request: Request,
    ride_id: int,
    db: Session = Depends(get_db),
    _: Annotated[None, Depends(_ops_session)] = None,
) -> HTMLResponse:
    ride = (
        db.query(RideRequest)
        .options(joinedload(RideRequest.venue_booking))
        .filter(RideRequest.id == ride_id)
        .first()
    )
    if ride is None:
        raise HTTPException(status_code=404, detail="Request not found.")
    return templates.TemplateResponse(
        request,
        "ops/request_detail.html",
        {"ride": ride, "booking": ride.venue_booking, "statuses": RideRequestStatus},
    )


@router.post("/requests/{ride_id}/status")
def ops_update_status(
    request: Request,
    ride_id: int,
    action: str = Form(...),
    ops_notes: str | None = Form(None),
    db: Session = Depends(get_db),
    _: Annotated[None, Depends(_ops_session)] = None,
) -> RedirectResponse:
    ride = db.get(RideRequest, ride_id)
    if ride is None:
        raise HTTPException(status_code=404, detail="Request not found.")

    action_map = {
        "whatsapp_sent": RideRequestStatus.WHATSAPP_SENT,
        "fulfilled": RideRequestStatus.FULFILLED,
        "declined": RideRequestStatus.DECLINED,
    }
    new_status = action_map.get(action)
    if new_status is None:
        raise HTTPException(status_code=400, detail="Invalid action.")

    update_ride_status(db, ride, new_status, ops_notes)
    return RedirectResponse(url=f"/ops/requests/{ride_id}", status_code=303)
