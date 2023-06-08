from fastapi import APIRouter, BackgroundTasks, Depends, Response, status
from app.auth.dependencies import (
    valid_refresh_token,
    valid_refresh_token_user,
    valid_user_create,
)
from app.auth.models import RefreshToken

from app.auth.schemas import (
    UserBaseReadSchema,
    UserAuthRegisterSchema,
    UserAuthLoginSchema,
    UserAccessTokenResponseSchema,
)
from app.auth.service import UserService
from app.users.models import User


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
) -> UserAccessTokenResponseSchema:
    pass


@router.put('/tokens')
async def refresh_token(
    worker: BackgroundTasks,
    response: Response,
    refresh_token: RefreshToken = Depends(valid_refresh_token),
    user: User = Depends(valid_refresh_token_user),
) -> UserAccessTokenResponseSchema:
    '''
    Endpoint for refreshing your access token with your refresh
    token if you lost your access token or someone stole it.
    '''
    pass


@router.delete('/logout')
async def logout_user(
    response: Response,
    refresh_token: RefreshToken = Depends(valid_refresh_token),
) -> dict:
    pass
