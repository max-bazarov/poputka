from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.auth.router import router as auth_router
from app.rides.bookings.router import router as bookings_router
from app.rides.router import router as rides_router

app = FastAPI(
    title='Попутка - поиск автомобильных попутчиков',
    root_path='/api'
)

origins = [
    "http://frontend:5000",  # React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", 
                   "Access-Control-Allow-Origin", "Authorization"],
)


app.include_router(auth_router)
app.include_router(rides_router)
app.include_router(bookings_router)
