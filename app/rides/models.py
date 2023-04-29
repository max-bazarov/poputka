from datetime import datetime
from sqlalchemy import (
    TIMESTAMP,
    Column,
    ForeignKey,
    Integer,
    String,
    DateTime,
)

from app.database import Base


class Ride(Base):
    __tablename__ = 'ride'

    id = Column(Integer, primary_key=True, nullable=False)
    driver = Column(ForeignKey('user.id'), nullable=False)
    car = Column(ForeignKey('car.id'), nullable=False)
    places = Column(Integer, nullable=False)
    destination_city = Column(String, nullable=False)
    distination_address = Column(String, nullable=False)
    departure_city = Column(String, nullable=False)
    departure_address = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    description = Column(String)


class Car(Base):
    __tablename__ = 'car'

    id = Column(Integer, primary_key=True, nullable=False)
    make = Column(String, nullable=False)
    model = Column(String, nullable=False)
    year = Column(Integer)
    license_plate_number = Column(String, nullable=False)
