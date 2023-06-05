from fastapi import APIRouter
from app.bookings.schemas import BookingReadSchema


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


# Получение списка своих бронирований.
@router.get('/bookings/{user_id}', response_model=list[BookingReadSchema])
async def get_my_bookings(user_id: int):
    pass


# Забронировать поездку.
@router.post('/{ride_id}/bookings', response_model=list[BookingReadSchema])
async def add_bookings(ride_id: int):
    pass


#  Узнать id-поездки.
@router.get('/id', response_model=list[BookingReadSchema])
async def get_bookings_id():
    pass


#  Отмена бронирования.
@router.delete('/rides/{ride_id}/bookings/{booking_id}/', response_model=list[BookingReadSchema])
async def delete_bookings_register(ride_id: int, booking_id: int):
    pass
