from app.core.service import BaseService
from app.rides.bookings.models import Booking


class BookingService(BaseService):
    model = Booking
