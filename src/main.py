from fastapi import FastAPI
import uvicorn
from configs.settings import settings
from routers.users_router import UsersRouter
from routers.dashboards.dashboards import DashboardsRouter
from routers.dashboards.folders import FoldersRouter
from routers.dashboards.connections import ConnectionsRouter
from routers.dashboards.queries import QueriesRouter
from auth.firebase import initialize_firebase
from contextlib import asynccontextmanager
from errors import handle_custom_exception
from errors import handle_validation_error
from fastapi.exceptions import RequestValidationError
from errors import CustomException


@asynccontextmanager
async def lifespan(_: FastAPI):
    print("Starting firebase admin")
    initialize_firebase()
    yield
    print("Closing app")


app = FastAPI(lifespan=lifespan)
app.include_router(UsersRouter)
app.include_router(DashboardsRouter)
app.include_router(FoldersRouter)
app.include_router(ConnectionsRouter)
app.include_router(QueriesRouter)
app.add_exception_handler(RequestValidationError, handle_validation_error)
app.add_exception_handler(CustomException, handle_custom_exception)


if __name__ == "__main__":
    uvicorn.run(app, host=settings.app_host, port=settings.app_port)
