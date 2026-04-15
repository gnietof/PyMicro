from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from app.models.member import DBMember, Member
from app.shared.db2.db2 import DB2Client


class MembersRepository(DB2Client):
    def get_members(self) -> list[Member] | None:
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session: 
            results = session.query(DBMember).all()
    
            return [Member.model_validate(row) for row in results]

    def get_member(self,id: str) -> Member | None:
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session:
            result = session.query(DBMember).filter(DBMember.id == id).first()
            if result:
                return Member.model_validate(result)
        return None
