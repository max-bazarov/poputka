from fastapi import APIRouter, status, Depends

from app.auth.dependencies import get_current_user

from app.users.schemas import (Profile, UserBase)
from app.users.service import UserService
from app.users.models import User

router = APIRouter(prefix='/users', tags=['Users'])


@router.get('/profile', response_model=Profile, status_code=status.HTTP_200_OK)
async def get_info_about_user_without_password_by_user_id(user: User = Depends(get_current_user)):
    result = await UserService.get_info_about_user_without_password(user.id)
    return result


@router.get('/users/', response_model=UserBase, status_code=status.HTTP_200_OK)
async def get_uuid_name_surname_age_likes_dislikes_reg_at_by_user_id(user_id: str):
    result = await UserService.get_uuid_name_surname_age_likes_dislikes_reg_at_by_uuid(user_id)
    return result
