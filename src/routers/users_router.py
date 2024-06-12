from fastapi import APIRouter
from settings import settings
from requests import make_request

UsersRouter = APIRouter(prefix="/v1/users", tags=["users"])


@UsersRouter.get("/")
async def hello_users():
    url = settings.users_service_url + "/v1/users"
    return await make_request(url, {}, "GET", {})
