from app.users.exceptions import EmailTakenException
from app.users.schemas import UserCreateSchema
from app.users.service import UserService


async def valid_user_create(user: UserCreateSchema) -> UserCreateSchema:
    if await UserService.get_object_or_none(email=user.email):
        raise EmailTakenException()

    return user
