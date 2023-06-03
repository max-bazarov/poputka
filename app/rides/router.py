from fastapi import APIRouter, Depends

from app.rides.schemas import RideCreateSchema, RideReadSchema
from app.rides.service import RidesService
# from app.users.auth_config import current_user
from app.users.models import User

router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('/rides')
async def get_rides() -> list[RideReadSchema]:
    pass


@router.get('/rides/{ride_id}')
async def get_ride_by_id() -> RideReadSchema:
    pass


@router.post('/rides/create')
async def create_ride() -> RideCreateSchema:
    pass


@router.delete('/rides/{ride_id}/delete')
async def delete_ride() -> RideReadSchema:
    pass
