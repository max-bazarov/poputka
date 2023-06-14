from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.rides.bookings.router import router as bookings_router
from app.rides.router import router as rides_router

app = FastAPI(
    title='Попутка - поиск автомобильных попутчиков',
    root_path='/api'
)

app.include_router(auth_router)
app.include_router(rides_router)
app.include_router(bookings_router)
