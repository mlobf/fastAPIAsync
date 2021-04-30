from pydantic import BaseModel
import enum


class Role(str, enum.Enum):
    admin: str = "admin"
    personal: str = "personal"


class User(BaseModel):
    name: str
    password: str
    mail: str
    role: Role
