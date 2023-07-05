from fastapi import APIRouter, status, Depends

from app.auth.dependencies import get_current_user

from app.users.schemas import (Profile, UserBase)
from app.users.models import User

from app.core.service import BaseService

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/profile', status_code=status.HTTP_200_OK)
async def get_current_user_private_info(user: User = Depends(get_current_user)) -> Profile:
    BaseService.model = User
    result = await BaseService.get_object_or_none(id=user.id)
    return result


@router.get('/users/{user_uuid}', status_code=status.HTTP_200_OK)
async def get_current_user_public_info(user_uuid: str) -> UserBase:
    BaseService.model = User
    result = await BaseService.get_object_or_none(id=user_uuid)
    return result
