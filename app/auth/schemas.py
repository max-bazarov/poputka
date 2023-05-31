from pydantic import BaseModel, EmailStr, validator, Field

from app.auth.utils import validate_password, validate_phone_number


class UserBaseReadSchema(BaseModel):
    email: EmailStr
    username: str

    class Config:
        orm_mode = True


class UserAuthRegisterSchema(BaseModel):
    name: str
    surname: str
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


class UserAuthLoginSchema(BaseModel):
    email: EmailStr
    password: str


class UserLoginAccessTokenResponseSchema(BaseModel):
    access_token: str
    refresh_token: str
