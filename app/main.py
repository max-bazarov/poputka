import aioredis

from fastapi import FastAPI
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache import FastAPICache

from app.auth.router import router as auth_router
from app.rides.bookings.router import router as bookings_router
from app.rides.router import router as rides_router


app = FastAPI(
    title='Попутка - поиск автомобильных попутчиков',
    root_path='/api'
)

app.include_router(auth_router)
app.include_router(rides_router)
app.include_router(bookings_router)


@app.on_event("startup")
async def startup_event():
    redis = aioredis.from_url("redis://localhost:6379", encoding="utf-8", decode_response=True)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
