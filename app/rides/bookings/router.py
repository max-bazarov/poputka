from app.rides.bookings.schemas import BookingReadSchema, BookingCreateSchema
from app.rides.router import router


@router.get('/bookings')
async def get_my_bookings() -> list[BookingReadSchema]:
    pass


@router.post('/{ride_id}/bookings')
async def add_booking(
    ride_id: int, new_booking: BookingCreateSchema
) -> BookingReadSchema:
    pass


@router.delete('/{ride_id}/bookings/{booking_id}')
async def delete_booking(ride_id: int, booking_id: int) -> BookingReadSchema:
    pass
