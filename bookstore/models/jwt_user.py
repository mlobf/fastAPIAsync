from pydantic import BaseModel


class JWTUser(BaseModel):
    username: str
    password: str
    disable: bool
    role: str
