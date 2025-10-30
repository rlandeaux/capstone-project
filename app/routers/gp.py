from fastapi import APIRouter
from starlette import status

from ..model.business_partner import BusinessPartner

gp_router = APIRouter()

@gp_router.post("/gp/", status_code=status.HTTP_201_CREATED)
async def create_gp(gp_data: BusinessPartner) -> None:
    pass