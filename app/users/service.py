from uuid import uuid4

from sqlalchemy import select

from app.core.service import BaseService
from app.database import async_session_maker
from app.users.models import User


class UserService(BaseService):
    model = User

    @classmethod
    async def get_info_about_user_without_password(cls, user_id: str):
        async with async_session_maker() as session:
            query = (
                select(cls.model.id, cls.model.email, cls.model.name, cls.model.surname, cls.model.phone_number,
                       cls.model.car_id, cls.model.age, cls.model.likes, cls.model.dislikes, cls.model.registered_at,
                       cls.model.is_admin, cls.model.is_active, cls.model.is_verified)
                .where(cls.model.id == user_id)
            )
            result = await session.execute(query)
            return result.mappings().one()

    @classmethod
    async def get_uuid_name_surname_age_likes_dislikes_reg_at_by_uuid(cls, user_id: str):
        async with async_session_maker() as session:
            query = (
                select(cls.model.id, cls.model.name, cls.model.surname, cls.model.age, cls.model.likes,
                       cls.model.dislikes, cls.model.registered_at)
                .where(cls.model.id == user_id)
            )
            result = await session.execute(query)
            return result.mappings().one()
