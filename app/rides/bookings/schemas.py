from datetime import datetime

from pydantic import BaseModel


class BookingReadSchema(BaseModel):
    id: int
    ride_id: int
    passenger_id: int
    created_at: datetime
    accepted_by_driver_at: str

