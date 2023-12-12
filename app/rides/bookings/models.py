from datetime import datetime

from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer

from app.db import Base


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, nullable=False)
    ride_id = Column(ForeignKey('ride.id'), nullable=False)
    passenger_id = Column(ForeignKey('user.id'), nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
    accepted_by_driver_at = Column(TIMESTAMP)
