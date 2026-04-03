from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from app.models.location import DBLocation, Location
from app.shared.db2.db2 import DB2Client


class LocationsRepository(DB2Client):
    def get_locations(self):
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session:
            # results = conn.execute(text("SELECT ID, FIRSTNAME, LASTNAME, WLC FROM ER_POPULATIONS.LOCATIONS"))
            results = session.query(DBLocation).all()
    
            return [Location.model_validate(row) for row in results]
        return None
        