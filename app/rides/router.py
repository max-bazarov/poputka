from fastapi import APIRouter

from app.rides.schemas import RideCreateSchema, RideReadSchema
from app.rides.service import RidesService


router = APIRouter(
    prefix='/rides',
    tags=['Rides']
)


@router.get('')
async def get_rides() -> list[RideReadSchema]:
    await RidesService.get_all()


@router.post('')
async def add_ride(
    new_ride: RideCreateSchema
):
    await RidesService.add(**new_ride)
