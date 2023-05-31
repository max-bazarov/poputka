from fastapi import APIRouter


router = APIRouter(
    prefix='/bookings',
    tags=['Бронирование поездок'],
)


# Получение списка своих бронирований .
@router.get('/my_bookings/register')
async def my_bookings_register():
    pass


# Забронировать поездку.
@router.post('/bookings/register')
async def bookings_register():
    pass


#  Узнать id-поездки.
@router.get('/bookings/id')
async def bookings_id():
    pass
