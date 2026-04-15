from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import ibm_db

from app.services.members.members import MembersRepository
from app.shared.db2 import db2
from app.settings import settings

app = FastAPI(title="Members Service")
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5000","http://localhost:5173"])

@app.get("/members")
def get_members():
    members = MembersRepository()
    rows = members.get_members()
    return rows

@app.get("/members/{id}")
def get_member(id: str):
    members = MembersRepository()
    member = members.get_member(id)
    return member