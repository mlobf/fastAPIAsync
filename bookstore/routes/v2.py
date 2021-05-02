from fastapi import FastAPI, Body, Header, File
from models.user import User
from models.author import Author
from models.book import Book
from starlette.status import HTTP_201_CREATED
from starlette.responses import Response

# Versioning are done at subproxis.

app_v2 = FastAPI(openapi_prefix="/v2")


"""
-> With Standard Header
@app_v2.post("/user")
async def post_user(user: User):
    return {"request body": user}
"""
# With Custom Header
@app_v2.post("/user", status_code=HTTP_201_CREATED)
async def post_user(user: User, x_custom: str = Header(...)):
    return {"request body": "Its version two"}


@app_v2.get("/user")
async def get_user_validation(password: str):
    return {"query parameter": password}
