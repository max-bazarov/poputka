from app.core.service import BaseService
from app.rides.models import Ride


class RidesService(BaseService):
    model = Ride
