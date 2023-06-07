from fastapi import APIRouter, status


from app.rides.schemas import RideCreateSchema, RideReadSchema


router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_rides() -> list[RideReadSchema]:
    pass


@router.get('/{ride_id}', status_code=status.HTTP_200_OK)
async def get_ride_by_id(ride_id) -> RideReadSchema:
    pass


@router.post('/new_ride', status_code=status.HTTP_201_CREATED)
async def create_ride(ride_id: int, new_ride: RideCreateSchema) -> RideReadSchema:
    pass


@router.delete('/{ride_id}', status_code=status.HTTP_201_DELETED)
async def delete_ride(ride_id: int) -> RideReadSchema:
    pass
