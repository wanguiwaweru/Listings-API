from sqlalchemy import Column, Integer, String
from database import Base


class Listing(Base):
    __tablename__ = "listings"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    address = Column(String, index=True)
    size = Column(String, index=True)
