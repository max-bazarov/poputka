from fastapi import APIRouter

from app.rides.schemas import RideReadSchema
from app.rides.service import RidesService

# from app.users.auth_config import current_user

router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('')
async def get_rides() -> list[RideReadSchema]:
    return await RidesService.get_all()


@router.post('/{ride_id}/bookings')
async def add_ride() -> list[RideReadSchema]:
    pass

# @router.post('')
# async def add_ride(
#     new_ride: RideCreateSchema, # user: User = Depends(current_user)
# ):
#     return await RidesService.create(user=user, **new_ride.dict())
