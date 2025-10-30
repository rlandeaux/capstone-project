import logging

from starlette.middleware.cors import CORSMiddleware
from app.routers import gp

from fastapi import FastAPI

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Business Partner API",
    description="Business Partner API",
    version="1.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)

app.include_router(router=gp.gp_router, tags=['Business Partner'])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Basic"])
async def hello_world():
    return {"Hello": "World"}