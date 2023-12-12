from typing import Annotated
from fastapi import APIRouter, Depends, Response, status

# from app.auth.config import auth_settings
from app.auth.dependencies import (
    auth_service_factory,
    # valid_refresh_token,
    # valid_refresh_token_user,
    valid_user_create,
)

# from app.auth.jwt import (
#     create_access_token,
#     create_refresh_token,
#     get_token_settings,
#     update_refresh_token,
# )
# from app.auth.models import RefreshToken
from app.auth.schemas import (
    AccessTokenResponseSchema,
    # UserLoginSchema,
    UserRegisterSchema,
)
from app.auth.service import AuthService

# from app.auth.utils import verify_user
# from app.auth.models import User

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def register_user(
    response: Response,
    users_service: Annotated[AuthService, Depends(auth_service_factory)],
    auth_data: UserRegisterSchema = Depends(valid_user_create),
) -> AccessTokenResponseSchema:
    access_token, refresh_token = await users_service.register_user(auth_data, response)

    return AccessTokenResponseSchema(
        access_token=access_token, refresh_token=refresh_token
    )


# @router.post("/login", status_code=status.HTTP_200_OK)
# async def login_user(
#     response: Response,
#     auth_data: UserLoginSchema,
# ) -> AccessTokenResponseSchema:
#     user = await UserService.authenticate_user(auth_data)
#     refresh_token_value = await create_refresh_token(user_id=user.id)
#     access_token_value = create_access_token(
#         user_id=user.id,
#     )

#     response.set_cookie(
#         **get_token_settings(
#             access_token_value,
#             auth_settings.ACCESS_TOKEN_KEY,
#             auth_settings.ACCESS_TOKEN_EXP,
#         )
#     )
#     response.set_cookie(
#         **get_token_settings(
#             refresh_token_value,
#             auth_settings.REFRESH_TOKEN_KEY,
#             auth_settings.REFRESH_TOKEN_EXP,
#         )
#     )

#     return AccessTokenResponseSchema(
#         access_token=access_token_value,
#         refresh_token=refresh_token_value,
#     )


# @router.put("/refresh")
# async def refresh_token(
#     response: Response,
#     refresh_token: RefreshToken = Depends(valid_refresh_token),
#     user: User = Depends(valid_refresh_token_user),
# ) -> AccessTokenResponseSchema:
#     """
#     Endpoint for refreshing your access token with your refresh
#     token if your access token is expired or someone stole your refresh token.
#     """
#     refresh_token_value = await update_refresh_token(old_refresh_token=refresh_token)
#     access_token_value = create_access_token(user_id=user.id)

#     response.set_cookie(
#         **get_token_settings(
#             refresh_token_value,
#             auth_settings.REFRESH_TOKEN_KEY,
#             auth_settings.REFRESH_TOKEN_EXP,
#         )
#     )

#     return AccessTokenResponseSchema(
#         access_token=access_token_value,
#         refresh_token=refresh_token_value,
#     )


# @router.delete("/logout", status_code=status.HTTP_200_OK)
# async def logout_user(
#     response: Response,
# ):
#     response.delete_cookie(auth_settings.ACCESS_TOKEN_KEY)
#     response.delete_cookie(auth_settings.REFRESH_TOKEN_KEY)


# @router.get("/verify", status_code=status.HTTP_200_OK)
# async def verify_email(token: str):
#     await verify_user(token=token)
