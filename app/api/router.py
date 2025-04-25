from fastapi import APIRouter
from app.api import phone, health

api_router = APIRouter()

api_router.include_router(phone.router)
api_router.include_router(health.router) 