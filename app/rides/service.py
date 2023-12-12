from sqlalchemy import insert

from app.core.service import BaseService
from app.db import async_session_maker
from app.rides.models import Ride
from app.users.models import User


class RidesService(BaseService):
    model = Ride

    @classmethod
    async def create(cls, user: User, **data):
        async with async_session_maker() as session:
            query = (
                insert(cls.model)
                .values(driver=user.id, **data)
                .returning(cls.model)
            )
            await session.execute(query)
            await session.commit()
