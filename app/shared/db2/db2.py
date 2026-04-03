from unittest import result
from urllib.parse import quote_plus

from pathlib import Path
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, text
from app.settings import settings

class DB2Client:
    def __init__(self):
        self._engine = None

    def get_engine(self):
        if self._engine is None:
            database_url = f"db2+ibm_db://{settings.DB2_USER}:{quote_plus(settings.DB2_PWD)}@{settings.DB2_HOST}:50001/BLUDB?SECURITY=SSL&SSLServerCertificate={self.get_cert_path()}"
            print(database_url)
            self._engine = create_engine(database_url)
        return self._engine

    def get_cert_path(self):
        cert_file = "certs/DigicertGlobalRootCAG5.crt"
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        return str(base_dir / cert_file)


