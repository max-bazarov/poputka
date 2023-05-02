from typing import Optional

from fastapi_users import schemas

from app.rides.schemas import CarReadSchema


class UserReadSchema(schemas.BaseUser[int]):
    id: int
    email: str
    username: str
    car: Optional[CarReadSchema]
    is_active: bool
    is_superuser: bool
    is_verified: bool

    class Config:
        orm_mode = True


class UserCreateSchema(schemas.BaseUserCreate):
    username: str
    email: str
    password: str
