from app.users.exceptions import EmailTakenException
from app.users.schemas import UserAuthSchema
from app.users.service import UserService


async def valid_user_create(user: UserAuthSchema) -> UserAuthSchema:
    if await UserService.get_object_or_none(email=user.email):
        raise EmailTakenException()

    return user
