from datetime import date

from sqlalchemy import and_, or_, select, insert
from sqlalchemy.ext.asyncio import session
from sqlalchemy.sql.functions import func
from app.core.service import BaseService
from app.exceptions import CannotBeBooked
from app.rides.bookings.models import Booking
from app.rides.models import Ride


class BookingService(BaseService):
    model = Booking

    @classmethod
    async def add(cls,
                  ride_id: int,
                  passenger_id: int,
                  created_at: date,
                  accept_by_driver_at: date):

        """
        WITH booked_ride AS (
	        SELECT * FROM bookings
	        WHERE ride_id = 1 AND
	        (created_at >= created_at AND created_at <= accept_by_driver_at) OR
	        (created_at <= created_at AND accept_by_driver_at > created_at)
        )
         """
        booked_ride = select(Booking).where(
                    and_(
                    Booking.room_id == 1,
                    or_(
                        and_(   
                            Booking.created_at >= created_at,
                            Booking.accepted_by_driver_at <= accept_by_driver_at
                        ),
                        and_(
                            Booking.created_at <= created_at,
                            Booking.accepted_by_driver_at > created_at
                        ),
                    )
                )
        ).cte("booked_ride")

        """
        SELECT ride.quantity - COUNT(booked_ride.ride_id) FROM ride
        LEFT JOIN booked_ride ON booked_ride.ride_id = ride_id
        WHERE ride.id = 1
        GROUP BY ride.quantity, booked_ride.ride_id
        """
        get_ride_left = select(
                (Ride.quantity - func.count(booked_ride.c.ride_id)).label("ride_left")
                ).select_from(Ride).join(
                    booked_ride, booked_ride.c.ride_id == Ride.id
                ).where(Ride.id == ride_id).group_by(
                    Ride.quantity, booked_ride.c.ride_id  
                )

        ride_left = await session.execute(get_ride_left)
        ride_left: int = ride_left.scalar()
        if ride_left > 0:
            add_booking = insert(Booking).values(
                    ride_id=ride_id,
                    passenger_id=passenger_id,
                    created_at=created_at,
                    accept_by_driver_at=accept_by_driver_at
                    ).returning(Booking)

            new_booking = await session.execute(add_booking)
            await session.commit()
            return new_booking.scalar()
        else:
            raise CannotBeBooked





