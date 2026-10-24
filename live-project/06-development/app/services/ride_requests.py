from sqlalchemy.orm import Session

from app.models.ride_request import RideRequest, RideRequestStatus
from app.models.venue_booking import VenueBooking


def create_ride_request(db: Session, booking: VenueBooking, pickup_area: str) -> RideRequest:
    ride = RideRequest(
        venue_booking_id=booking.id,
        pickup_area=pickup_area.strip(),
        status=RideRequestStatus.NEW,
    )
    db.add(ride)
    db.commit()
    db.refresh(ride)
    return ride


def update_ride_status(
    db: Session,
    ride: RideRequest,
    new_status: RideRequestStatus,
    ops_notes: str | None = None,
) -> RideRequest:
    ride.status = new_status
    if ops_notes is not None:
        trimmed = ops_notes.strip()
        ride.ops_notes = trimmed if trimmed else None
    db.commit()
    db.refresh(ride)
    return ride
