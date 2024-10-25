from pydantic import BaseModel
from typing import Optional


class ListingBase(BaseModel):
    name: str
    address: str
    size: str


class ListingCreate(ListingBase):
    pass


class Listing(ListingBase):
    id: int

    class Config:
        from_attributes = True


"""arbitrary_types_allowed = True
schema_extra = {
    "example": {
        "name": "JaneDoe",
        "address": "First Avenue",
        "size": "1 bedroom"
    }
}"""
