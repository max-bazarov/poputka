from fastapi import Depends

from app.auth.dependencies import get_current_ride
from app.rides.bookings.schemas import BookingReadSchema, BookingCreateSchema
from app.rides.bookings.service import BookingService
from app.rides.models import Ride
from app.rides.router import router


@router.get('/bookings/{ride_id}')
async def get_my_bookings(ride_id: int, ride: Ride = Depends()) -> list[BookingReadSchema]:
    return await BookingService.get_all(ride_id=ride.id)


@router.post('/{ride_id}/bookings')
async def add_booking(
    ride_id: int, new_booking: BookingCreateSchema
) -> BookingReadSchema:
    pass


@router.delete('/{ride_id}/bookings/{booking_id}')
async def delete_booking(ride_id: int, booking_id: int) -> BookingReadSchema:
    pass
