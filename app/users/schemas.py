from dataclasses import Field

from pydantic import BaseModel, EmailStr, validator

from app.users.utils import validate_password


class UserBaseReadSchema(BaseModel):
    email: EmailStr
    username: str

    class Config:
        orm_mode = True


class UserCreateSchema(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(min_length=6, max_length=128)

    @validator('password')
    def validate_password(cls, password: str) -> str:
        validate_password(password)

        return password
