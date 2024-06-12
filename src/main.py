from fastapi import FastAPI
import uvicorn
from settings import settings
from routers.users_router import UsersRouter

app = FastAPI()
app.include_router(UsersRouter)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)
