from pydantic import BaseModel


class Envs(BaseModel):
    # todo разбить на server config и сlient config
    frontend_url: str
    gateway_url: str
    auth_url: str
    auth_secret: str
    spend_db_url: str
    test_username: str
    test_password: str
