from fastapi import APIRouter
from app.bookings.schemas import BookingReadSchema


router = APIRouter(
    prefix='/bookings',
    tags=['Bookings'],
)


# Получение списка своих бронирований.
@router.get('/my_bookings/register', response_model=list[BookingReadSchema])
async def my_bookings_register():
    pass


# Забронировать поездку.
@router.post('/{ride_id}/bookings', response_model=list[BookingReadSchema])
async def bookings_register(ride_id: int):
    pass


#  Узнать id-поездки.
@router.get('/id', response_model=list[BookingReadSchema])
async def bookings_id():
    pass
