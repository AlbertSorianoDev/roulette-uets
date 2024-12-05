from fastapi import FastAPI

from src.api.v1.routers.main_router import api_v1_router

api_v1 = FastAPI()
api_v1.title = "Roulette UETS API v1"
api_v1.version = "0.0.1"

api_v1.include_router(api_v1_router)
