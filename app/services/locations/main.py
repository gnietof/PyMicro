from pathlib import Path
from pydantic import BaseModel
from typing_extensions import Annotated
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import ibm_db

from app.models.location import LocationFilterParams
from app.services.locations.locations import LocationsRepository
from app.services.members.members import MembersRepository
from app.shared.db2 import db2
from app.settings import settings

app = FastAPI(title="Locations Service")
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["http://localhost:5000","http://localhost:5173"])

@app.get("/locations")
def get_locations(filter_query: Annotated[LocationFilterParams, Query()]):

    locations = LocationsRepository()
    rows = locations.get_locations(filter_query)
    
    return rows

@app.get("/location/{wlc}")
def get_locations(wlc: str):
    locations = LocationsRepository()
    rows = locations.get_location(wlc)
    
    return rows

@app.get("/locations/countries")
def get_countries():
    locations = LocationsRepository()
    countries = locations.get_countries()
    return countries



