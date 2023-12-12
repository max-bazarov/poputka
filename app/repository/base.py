from abc import ABC, abstractmethod
from httpx import delete

from sqlalchemy import insert, select, update
from app.db import async_session_maker, Base


class AbstractRepository(ABC):
    @abstractmethod
    async def get_one_or_none():
        raise NotImplementedError

    @abstractmethod
    async def get_all():
        raise NotImplementedError

    @abstractmethod
    async def create():
        raise NotImplementedError

    @abstractmethod
    async def update():
        raise NotImplementedError

    @abstractmethod
    async def delete():
        raise NotImplementedError


class SQLAlchemyRepository(AbstractRepository):
    model: Base = None

    async def get_one_or_none(self, **filter_by):
        async with async_session_maker() as session:
            query = select(self.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().one_or_none()

    async def get_all(self, **filter_by):
        async with async_session_maker() as session:
            query = select(self.model.__table__.columns).filter_by(**filter_by)
            result = await session.execute(query)
            return result.mappings().all()

    async def create(self, **data):
        async with async_session_maker() as session:
            query = insert(self.model).values(**data).returning(self.model)
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    async def update(self, *, id: int, **data):
        async with async_session_maker() as session:
            query = (
                update(self.model)
                .where(self.model.id == id)
                .values(**data)
                .returning(self.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.mappings().first()

    async def delete(self, *, id: int):
        async with async_session_maker() as session:
            query = delete(self.model).where(self.model.id == id)
            await session.execute(query)
            await session.commit()
