from app.rides.bookings.schemas import BookingReadSchema
from app.rides.router import router


# Получение списка своих бронирований.
@router.get('/bookings', response_model=list[BookingReadSchema])
async def get_my_bookings():
    pass


# Забронировать поездку.
@router.post('/{ride_id}/bookings', response_model=list[BookingReadSchema])
async def add_bookings(ride_id: int):
    pass


#  Отмена бронирования.
@router.delete('/rides/{ride_id}/bookings/{booking_id}/', response_model=BookingReadSchema)
async def delete_booking(ride_id: int, booking_id: int):
    pass
