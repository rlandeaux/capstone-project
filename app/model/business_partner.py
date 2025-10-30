import datetime

from pydantic import BaseModel, EmailStr
from uuid import UUID


class BusinessPartner(BaseModel):
    """
    BaseModel for business partners containing basic master data like Name and Address as such a unique id
    """
    id: UUID
    create_date: datetime.date
    first_name: str
    middle_name: str | None
    last_name: str
    email: EmailStr
    street: str
    house_number: str
    city: str
    zipcode: str
    country: str