from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    DB2_HOST: str
    DB2_USER: str
    DB2_PWD: str

    class Config:
        env_file="../.env"

settings = Settings()