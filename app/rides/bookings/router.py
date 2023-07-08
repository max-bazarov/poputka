from fastapi import Depends
from app.auth.dependencies import get_current_user
from app.rides.bookings.schemas import BookingCreateSchema, BookingReadSchema
from app.rides.bookings.service import BookingService
from app.rides.router import router
from app.users.models import User


@router.get('/{ride_id}/bookings')
async def get_bookings(ride_id: int) -> list[BookingReadSchema]:
    return await BookingService.get_all(ride_id=ride_id)


@router.post('/{ride_id}/bookings')
async def add_booking(
    ride_id: int, new_booking: BookingCreateSchema, user: User = Depends(get_current_user())
) -> BookingReadSchema:
    booking = await BookingService.create(**new_booking.dict(), user.id)
    return booking


@router.delete('/{ride_id}/bookings/{booking_id}')
async def delete_booking(ride_id: int, booking_id: int) -> BookingReadSchema:
    pass
