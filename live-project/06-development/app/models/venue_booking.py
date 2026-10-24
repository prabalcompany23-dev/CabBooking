from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db import Base


class VenueBooking(Base):
    __tablename__ = "venue_bookings"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    player_name: Mapped[str] = mapped_column(String(120), nullable=False)
    contact: Mapped[str] = mapped_column(String(80), nullable=False)
    city: Mapped[str] = mapped_column(String(80), nullable=False)
    sport: Mapped[str] = mapped_column(String(80), nullable=False)
    venue_name: Mapped[str] = mapped_column(String(200), nullable=False)
    game_starts_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    own_vehicle: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)

    ride_requests: Mapped[list["RideRequest"]] = relationship(
        "RideRequest", back_populates="venue_booking"
    )


from app.models.ride_request import RideRequest  # noqa: E402
