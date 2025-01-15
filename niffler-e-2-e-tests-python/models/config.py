import os

from dotenv import load_dotenv
from pydantic import BaseModel


class Envs(BaseModel):
    frontend_url: str
    gateway_url: str
    auth_url: str
    auth_secret: str
    spend_db_url: str
    test_username: str
    test_password: str
    kafka_address: str
