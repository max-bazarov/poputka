from fastapi import APIRouter, Depends, Response, status
from app.users.dependencies import valid_user_create

from app.users.schemas import (
    UserBaseReadSchema,
    UserAuthSchema,
    UserLoginAccessTokenResponseSchema,
)
from app.users.service import UserService


router = APIRouter(prefix='/auth', tags=['Авторизация'])


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
    auth_data: UserAuthSchema = Depends(valid_user_create),
) -> UserBaseReadSchema:
    user = await UserService.create(auth_data)
    return {
        'email': user['email'],
        'username': user['username'],
    }


@router.post('/login')
async def login_user(
    auth_data: UserAuthSchema, response: Response
) -> UserLoginAccessTokenResponseSchema:
    pass
