from passlib.context import CryptContext
from models.jwt_user import JWTUser


pwd_context = CryptContext(schemes=["bcrypt"])
jwt_user1 = {
    "username": "user1",
    "password": "pass1",
    "disabled": False,
    "role": "admin",
}
# fake_jwt_user1 = JWTUser(**jwt_user1)


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return False


hashed = "$2b$12$KfVXIOtPV0lVjLmD1QEodO2BQpbMZu7G0KGUzMuIi.PzORF1hekYC"

# print(verify_password("mysecret", hashed))

"""
  Authenticate username password to give JWT Token.
"""


def authenticate_user(username: str, password: str):
    pass


"""
  Create Access JWT Token.
"""


"""
  Check id the JWT Token is correct or not.
"""

"""
  Last checking and returning the final result.
"""
print(get_hashed_password("pass1"))
