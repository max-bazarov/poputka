from app.rides.bookings.schemas import BookingReadSchema
from app.rides.router import router


# Получение списка своих бронирований.
@router.get('/bookings')
async def get_my_bookings() -> list[BookingReadSchema]:
    pass


# Забронировать поездку.
@router.post('/{ride_id}/booking')
async def add_booking(ride_id: int) -> BookingReadSchema:
    pass


#  Отмена бронирования.
@router.delete('/rides/{ride_id}/bookings/{booking_id}/')
async def delete_booking(ride_id: int, booking_id: int) -> BookingReadSchema:
    pass
