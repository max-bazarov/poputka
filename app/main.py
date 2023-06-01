from fastapi import FastAPI

from app.rides.router import router as rides_router

from app.bookings.router import router as bookings_router

from app.auth.router import router as users_router

app = FastAPI(
    title='Попутка - поиск автомобильных попутчиков',
)

app.include_router(users_router)
app.include_router(rides_router)
app.include_router(bookings_router)
