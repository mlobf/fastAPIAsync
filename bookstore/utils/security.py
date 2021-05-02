from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"])


def get_hashed_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    try:
        return pwd_context.verify(plain_password, hashed_password)
    except Exception as e:
        return False


hashed = "$2b$12$KfVXIOtPV0lVjLmD1QEodO2BQpbMZu7G0KGUzMuIi.PzORF1hekYC"

print(verify_password("mysecret", hashed))
