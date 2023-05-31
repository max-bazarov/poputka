from typing import Dict, Any

from fastapi import APIRouter, Depends, status
from app.users.dependencies import valid_user_create

from app.users.schemas import UserBaseReadSchema, UserCreateSchema
from app.users.service import UserService


router = APIRouter(prefix='/auth', tags=['Авторизация'])


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
    auth_data: UserCreateSchema = Depends(valid_user_create),
) -> dict[str, Any]:
    user = await UserService.create(auth_data)
    return {
        'email': user['email'],
        'username': user['username'],
    }
