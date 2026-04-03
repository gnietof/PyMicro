from pathlib import Path

from fastapi import FastAPI
import ibm_db

from app.services.locations.locations import LocationsRepository
from app.services.members.members import MembersRepository
from app.shared.db2 import db2
from app.settings import settings

app = FastAPI(title="Members Service")

@app.get("/locations")
def get_locations():

    # dsn = (
    #     "DATABASE=BLUDB;"  # Replace with your database name
    #     f"HOSTNAME={settings.DB2_HOST};"  # Replace with your DB2 host
    #     "PORT=50001;"  # Replace with your port (default is 50001)
    #     "PROTOCOL=TCPIP;"
    #     f"UID={settings.DB2_USER};"  # Replace with your username
    #     f"PWD={settings.DB2_PWD};"  # Replace with your password
    #     "SECURITY=SSL;"  # Use SSL for secure connection
    #     f"SSLServerCertificate={get_cert_path()};"
    # )

    # rows = []
    # conn = ibm_db.connect(dsn, "", "")
    # sql = "SELECT ID, FIRSTNAME, LASTNAME, WLC FROM ER_POPULATIONS.MEMBERS"
    # stmt = ibm_db.exec_immediate(conn, sql)
    # row = ibm_db.fetch_assoc(stmt)
    # while row:
    #     rows.append(row)
    #     row = ibm_db.fetch_assoc(stmt)
    # ibm_db.close(conn)

    locations = LocationsRepository()
    rows = locations.get_locations()
    
    return rows