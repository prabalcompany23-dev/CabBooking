import enum
from datetime import datetime

from sqlalchemy import DateTime, Enum, ForeignKey, Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class RideRequestStatus(str, enum.Enum):
    NEW = "NEW"
    WHATSAPP_SENT = "WHATSAPP_SENT"
    FULFILLED = "FULFILLED"
    DECLINED = "DECLINED"


class RideRequest(Base):
    __tablename__ = "ride_requests"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    venue_booking_id: Mapped[int] = mapped_column(ForeignKey("venue_bookings.id"), nullable=False)
    pickup_area: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[RideRequestStatus] = mapped_column(
        Enum(RideRequestStatus, native_enum=False, length=20),
        default=RideRequestStatus.NEW,
        nullable=False,
    )
    ops_notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False
    )

    venue_booking: Mapped["VenueBooking"] = relationship(
        "VenueBooking", back_populates="ride_requests"
    )


from app.models.venue_booking import VenueBooking  # noqa: E402
