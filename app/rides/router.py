from fastapi import APIRouter, Depends

from app.rides.schemas import RideCreateSchema, RideReadSchema
from app.rides.service import RidesService
# from app.users.auth_config import current_user
from app.users.models import User

router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('')
async def get_rides() -> list[RideReadSchema]:
    return await RidesService.get_all()


# @router.post('')
# async def add_ride(
#     new_ride: RideCreateSchema, # user: User = Depends(current_user)
# ):
#     return await RidesService.create(user=user, **new_ride.dict())
