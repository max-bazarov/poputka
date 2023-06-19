from datetime import datetime

from app.auth.exceptions import EmailTakenException, TokenAbsentException
from app.auth.schemas import UserAuthRegisterSchema
from app.auth.service import UserService
from fastapi import Request, Depends
from jose import jwt, JWTError

from app.rides.service import RidesService
from app.users import config


async def valid_user_create(
    user: UserAuthRegisterSchema,
) -> UserAuthRegisterSchema:
    if await UserService.get_object_or_none(email=user.email):
        raise EmailTakenException()

    return user


async def valid_refresh_token():
    pass


async def valid_refresh_token_user():
    pass


async def get_token(request: Request):
    token = request.cookies.get('ACCESS_TOKEN_KEY')
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(token: str = Depends(get_token)):
    try:
        payload = jwt.decode(token, config.JWT_SECRET, config.JWT_ALG)

    except JWTError:
        raise TokenAbsentException

    expire: str = payload.get('exp')
    if (not expire) or (int(expire) < datetime.utcnow().timestamp()):
        raise TokenAbsentException
    ride_id: str = payload.get('sub')
    if not ride_id:
        raise TokenAbsentException
    ride = await RidesService.get_object_or_none(int(ride_id))
    if not ride:
        raise TokenAbsentException
    return ride

