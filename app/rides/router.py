from fastapi import APIRouter, status

from app.rides.schemas import (
    RideCreateSchema,
    RideReadSchema,
    RideUpdateSchema,
)


router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_rides() -> list[RideReadSchema]:
    pass


@router.get('/{ride_id}', status_code=status.HTTP_200_OK)
async def get_ride(ride_id: int) -> RideReadSchema:
    pass


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_ride(
    ride_id: int, new_ride: RideCreateSchema
) -> RideReadSchema:
    pass


@router.patch('/{ride_id}', status_code=status.HTTP_200_OK)
async def update_ride(
    ride_id: int, updated_ride: RideUpdateSchema
) -> RideReadSchema:
    pass


@router.delete('/{ride_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_ride(ride_id: int):
    pass
