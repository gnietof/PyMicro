
from pydantic import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class DBMember(Base):
    __tablename__ = "MEMBERS"
    __table_args__ = {"schema": "ER_POPULATIONS"}

    id = Column("ID", String(9), primary_key=True)
    first_name = Column("FIRSTNAME", String(64))
    last_name = Column("LASTNAME", String(64))
    email = Column("EMAIL", String(100))
    manager = Column("MANAGER", String(9))
    wlc = Column("WLC", String(3))

class Member(BaseModel):
    id: str
    first_name: str
    last_name: str
    email: str
    manager: str
    wlc: str

    class Config:
        from_attributes = True
    
