
from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DBLocation(Base):
    __tablename__ = "LOCS"
    __table_args__ = {"schema": "ER_POPULATIONS"}

    id = Column("WLC", String, primary_key=True)
    campus_name = Column("CAMPUS_NAME", String(64))
    campus_id = Column("CAMPUS_ID", String(64))
    geo = Column("GEO", String(100))
    country = Column("COUNTRY", String(100))
    city = Column("CITY", String(100))

class Location(BaseModel):
    id: str
    campus_name: str
    campus_id: str
    geo: str
    country: str
    city: str

    class Config:
        from_attributes = True

