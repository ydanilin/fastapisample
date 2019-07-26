from fastapi import FastAPI
from starlette.requests import Request

from app.core import config
from .db.session import Session
from .api.api_v1.api import api_router


app = FastAPI(title=config.PROJECT_NAME, openapi_url="/api/v1/openapi.json")
app.include_router(api_router, prefix=config.API_V1_STR)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    request.state.db = Session()
    response = await call_next(request)
    request.state.db.close()
    return response


# for development run with debugger
if __name__ == "__main__":
    import uvicorn  # noqa
    uvicorn.run(app, host="0.0.0.0", port=8000)
