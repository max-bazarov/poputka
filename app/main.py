from fastapi import FastAPI

from app.rides.router import router as rides_router
from app.users.auth_config import auth_backend, fastapi_users
from app.users.schemas import UserCreateSchema, UserReadSchema

app = FastAPI(title='Попутка - поиск автомобильных попутчиков')


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserReadSchema, UserCreateSchema),
    prefix="/auth",
    tags=["Auth"],
)

app.include_router(rides_router)
