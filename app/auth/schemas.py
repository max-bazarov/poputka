from typing import Optional

from pydantic import BaseModel, EmailStr, Field, validator

from app.auth.validators import validate_password, validate_phone_number


class UserBaseReadSchema(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


class UserAuthRegisterSchema(BaseModel):
    name: str
    surname: Optional[str] = None
    email: EmailStr
    phone_number: str = Field(min_length=11, max_length=20)
    age: int
    password: str = Field(min_length=6, max_length=128)

    @validator('password')
    def validate_password(cls, password: str) -> str:
        validate_password(password)

        return password

    @validator('phone_number')
    def validate_phone_number(cls, phone_number: str) -> str:
        validate_phone_number(phone_number)

        return phone_number

    class Config:
        schema_extra = {
            'example': {
                'name': 'Ivan',
                'surname': 'Ivanov',
                'age': 25,
                'phone_number': '+79123456789',
                'email': 'ivanov@gmail.com',
                'password': 'Password1234!',
            }
        }


class UserAuthLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserAccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
