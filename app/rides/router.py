from fastapi import APIRouter, status


from app.rides.schemas import RideCreateSchema, RideReadSchema, RideDeleteSchema, RideUpdateSchema


router = APIRouter(prefix='/rides', tags=['Rides'])


@router.get('/', status_code=status.HTTP_200_OK)
async def get_rides() -> list[RideReadSchema]:
    pass


@router.get('/ride_id/<id>', status_code=status.HTTP_200_OK)
async def get_ride(ride_id: int) -> RideReadSchema:
    pass


@router.post('/create_ride', status_code=status.HTTP_201_CREATED)
async def create_ride(ride_id: int, new_ride: RideCreateSchema) -> RideReadSchema:
    pass


@router.put('/update_ride/<id>', status_code=status.HTTP_200_OK)
async def update_ride(ride_id: int, updated_ride: RideUpdateSchema) -> RideReadSchema:
    pass


@router.delete('/delete_ride/<id>', status_code=status.HTTP_201_DELETED)
async def delete_ride(ride_id: int, deleted_ride: RideDeleteSchema) -> RideReadSchema:
    pass
