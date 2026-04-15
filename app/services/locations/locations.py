from typing import Annotated

from fastapi import Query
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

from app.models.location import DBLocation, Location, LocationFilterParams
from app.shared.db2.db2 import DB2Client


class LocationsRepository(DB2Client):
    def get_locations(self, filter_query: Annotated[LocationFilterParams, Query()]= None) -> list[Location] | None:
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session:
            query = session.query(DBLocation)
            if filter_query.country:
                query = query.filter(DBLocation.country == filter_query.country)
            if filter_query.city:
                query = query.filter(DBLocation.city == filter_query.city)  
            if filter_query.wlc:
                query = query.filter(DBLocation.wlc == filter_query.wlc)  
            results = query.all()

            return [Location.model_validate(row) for row in results]
        return None
        

    def get_location(self, wlc: str) -> Location | None:
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session:
            result = session.query(DBLocation).filter(DBLocation.wlc == wlc).first()

            if result:
                return Location.model_validate(result)
        return None

    def get_countries(self):
        SessionLocal = sessionmaker(bind=self.get_engine())

        with SessionLocal() as session:
            stmt = session.query(DBLocation.country).distinct()

            return [row[0] for row in stmt.all()]
        return None        