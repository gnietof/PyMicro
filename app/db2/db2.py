from unittest import result
from urllib.parse import quote_plus

from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from app.settings import settings

def get_engine():

    database_url = f"db2+ibm_db://{settings.DB2_USER}:{quote_plus(settings.DB2_PWD)}@{settings.DB2_HOST}:50001/BLUDB?SECURITY=SSL&SSLServerCertificate={get_cert_path()}"
    print(database_url)

    engine = create_engine(database_url)
    return engine

    # SessionLocal = sessionmaker(bind=engine)

    # db = SessionLocal()

    # try: 
    #     yield db
    # finally:
    #     db.close()

def get_members():
    with get_engine().connect() as conn:
        result = conn.execute(text("SELECT ID, FIRSTNAME, LASTNAME, WLC FROM ER_POPULATIONS.MEMBERS"))

        rows = [dict(row._mapping) for row in result]
        
    return rows 
 
def get_cert_path():
    # cert_file = "../../certs/DigicertGlobalRootCAG5.crt"
    cert_file = "certs/DigicertGlobalRootCAG5.crt"
    base_dir = Path(__file__).resolve().parent.parent.parent
    return str(base_dir / cert_file)


