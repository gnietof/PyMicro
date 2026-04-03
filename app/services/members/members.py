from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from app.models.member import DBMember, Member
from app.shared.db2.db2 import DB2Client


class MembersRepository(DB2Client):
    def get_members(self):
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session:
            # results = conn.execute(text("SELECT ID, FIRSTNAME, LASTNAME, WLC FROM ER_POPULATIONS.LOCATIONS"))
            results = session.query(DBMember).all()
    
            return [Member.model_validate(row) for row in results]
        return None
        