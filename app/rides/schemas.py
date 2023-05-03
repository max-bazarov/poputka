from datetime import date, time, datetime

from pydantic import BaseModel


class CarReadSchema(BaseModel):
    id: int
    make: str
    model: str
    year: int
    license_plate_number: str


class RideReadSchema(BaseModel):
    id: int
    driver: int
    car: CarReadSchema
    places: int
    destination_city: str
    destination_address: str
    departure_city: str
    departure_address: str
    time: time
    date: date
    created_at: datetime
    description: str

    class Config:
        orm_mode = True


class RideCreateSchema(BaseModel):
    driver: int
    car: int
    places: int
    destination_city: str
    destination_address: str
    departure_city: str
    departure_address: str
    time: time
    date: date
    description: str

    class Config:
        orm_mode = True
