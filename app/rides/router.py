from fastapi import APIRouter, Depends

from app.rides.schemas import RideCreateSchema, RideReadSchema
from app.rides.service import RidesService
# from app.users.auth_config import current_user
from app.users.models import User

router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('/')
async def get_rides() -> list[RideReadSchema]:
    pass
    # return await RidesService.get_all()


@router.get('/<ride_id:int>')
async def get_ride_by_id() -> RideReadSchema:
    pass


@router.post('/create')
async def create_ride() -> RideCreateSchema:
    pass


@router.delete('/delete')
async def delete_ride():  # should be return RideDeleteSchema (in process)
    pass
