from fastapi import APIRouter
from app.api.v1.endpoints import health, cycles, content

api_router = APIRouter()

api_router.include_router(health.router, tags=["health"])
api_router.include_router(cycles.router, prefix="/cycles", tags=["cycles"])
api_router.include_router(content.router, prefix="/content", tags=["content"])
