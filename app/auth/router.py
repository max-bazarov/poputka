from fastapi import APIRouter, Depends, Response, status
from app.auth.dependencies import valid_user_create

from app.auth.schemas import (
    UserBaseReadSchema,
    UserAuthRegisterSchema,
    UserAuthLoginSchema,
    UserLoginAccessTokenResponseSchema,
)
from app.auth.service import UserService


router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/register', status_code=status.HTTP_201_CREATED)
async def register_user(
    auth_data: UserAuthRegisterSchema = Depends(valid_user_create),
) -> UserBaseReadSchema:
    user = await UserService.create(auth_data)
    return {
        'email': user['email'],
        'username': user['username'],
    }


@router.post('/login')
async def login_user(
    auth_data: UserAuthLoginSchema, response: Response
) -> UserLoginAccessTokenResponseSchema:
    pass
