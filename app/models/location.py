
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Numeric, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DBLocation(Base):
    __tablename__ = "LOCS"
    __table_args__ = {"schema": "ER_POPULATIONS"}

    wlc = Column("WLC", String, primary_key=True)
    campus_name = Column("CAMPUS_NAME", String(64))
    campus_id = Column("CAMPUS_ID", String(64))
    geo = Column("GEO", String(100))
    country = Column("COUNTRY", String(100))
    city = Column("CITY", String(100))
    latitude = Column("LATITUDE", Numeric(10, 6))
    longitude = Column("LONGITUDE", Numeric(10, 6))
    virtual = Column("VIRTUAL", String(1))

class Location(BaseModel):
    wlc: str
    campus_name: str
    campus_id: str
    geo: str
    country: str
    city: str
    latitude: float
    longitude: float
    virtual: str

    class Config:
        from_attributes = True

class LocationFilterParams(BaseModel):
    country: Optional[str] = None
    city: Optional[str] = None
    wlc: Optional[str] = None
