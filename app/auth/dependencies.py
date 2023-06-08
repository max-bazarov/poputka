from app.auth.exceptions import EmailTakenException
from app.auth.schemas import UserAuthRegisterSchema
from app.auth.service import UserService


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
