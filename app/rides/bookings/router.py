from app.rides.bookings.schemas import BookingCreateSchema, BookingReadSchema
from app.rides.bookings.service import BookingService
from app.rides.router import router


@router.get('/{ride_id}/bookings')
async def get_bookings(ride_id: int) -> list[BookingReadSchema]:
    return await BookingService.get_all(ride_id=ride_id)


@router.post('/{ride_id}/bookings')
async def add_booking(
    ride_id: int, new_booking: BookingCreateSchema
) -> BookingReadSchema:
    pass


@router.delete('/{ride_id}/bookings/{booking_id}')
async def delete_booking(ride_id: int, booking_id: int) -> BookingReadSchema:
    pass
