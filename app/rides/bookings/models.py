from app.database import Base

from sqlalchemy import Integer, Column, ForeignKey, TIMESTAMP


class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, nullable=False)
    ride_id = Column(ForeignKey('ride.id'), nullable=False)
    passenger_id = Column(ForeignKey('user.id'), nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)
    accepted_by_driver_at = Column(TIMESTAMP, nullable=False)

