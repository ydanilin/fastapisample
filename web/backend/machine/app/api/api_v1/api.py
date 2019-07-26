from fastapi import APIRouter
from .endpoints import login, countries

api_router = APIRouter()
api_router.include_router(
    login.router, prefix="/oauth", tags=["login"]
)
api_router.include_router(
    countries.router, prefix="/countries", tags=["countries"]
)
