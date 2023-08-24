from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection
from redis_om import HashModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)


redis = get_redis_connection(
    host = "",
    port = "",
    password = "",
    decode_responses = True
)


class Delivery(HashModel):
    budget: int = 0
    notes: str = ""
    class Meta:
        database = redis
    

class Event(HashModel):
    delivery_id: str = None
    type: str
    data: str

    class Meta:
        database = redis


