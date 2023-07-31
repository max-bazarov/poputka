from datetime import datetime

from fastapi import Depends, Request
from fastapi.params import Cookie
from jose import JWTError, jwt

from app.auth.config import config
from app.auth.exceptions import (
    EmailTakenException,
    RefreshTokenNotValid,
    TokenAbsentException,
)
from app.auth.models import RefreshToken
from app.auth.schemas import UserAuthRegisterSchema
from app.auth.service import RefreshTokenService, UserService
from app.users.models import User


async def valid_user_create(
    user: UserAuthRegisterSchema,
) -> UserAuthRegisterSchema:
    if await UserService.get_object_or_none(email=user.email):
        raise EmailTakenException()

    return user


async def valid_refresh_token(
    refresh_token: str = Cookie(alias=config.REFRESH_TOKEN_KEY),
) -> RefreshToken:
    db_refresh_token = await RefreshTokenService.get_object_or_none(
        refresh_token=refresh_token
    )

    if not db_refresh_token:
        raise RefreshTokenNotValid()

    if not await _is_valid_refresh_token(db_refresh_token):
        raise RefreshTokenNotValid()

    return db_refresh_token


async def valid_refresh_token_user(
    refresh_token: str = Depends(valid_refresh_token),
) -> User:
    user = await UserService.get_object_or_none(id=refresh_token.user_id)
    if not user:
        raise RefreshTokenNotValid()

    return user


async def _is_valid_refresh_token(refresh_token: RefreshToken):
    return datetime.utcnow() <= refresh_token.expires_at


async def get_token(request: Request):
    token = request.cookies.get(config.ACCESS_TOKEN_KEY)
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
    user_id: str = payload.get('sub')
    if not user_id:
        raise TokenAbsentException
    user = await UserService.get_object_or_none(int(user_id))
    if not user:
        raise TokenAbsentException
    return user
