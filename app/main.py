from fastapi import FastAPI

from app.rides.router import router as rides_router
from app.users.router import router as users_router

app = FastAPI(
    title='Попутка - поиск автомобильных попутчиков',
)

app.include_router(users_router)
app.include_router(rides_router)
