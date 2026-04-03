
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Member(Base):
    __tablename__ = "MEMBERS"
    __schemaname__ = "ER_POPULATIONS"

    id = Column(String,primary_key=True)
    first_name = Column(String(64))
    last_name = Column(String(64))
    email = Column(String(100))

    