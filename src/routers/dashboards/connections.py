from fastapi import APIRouter
from configs.settings import settings
from request import make_request
from auth.firebase import get_firebase_user
from fastapi import Depends, Request
from schemas.connections import (
    CreateConnection,
    UpdateConnection,
    GetConnections,
    GetUserConnections,
)

ConnectionsRouter = APIRouter(tags=["connections"])

URL = settings.dashboards_service_url


@ConnectionsRouter.post("/{version}/connections")
async def create_connection(
    request: Request,
    request_body: CreateConnection,
    version: str,
    user=Depends(get_firebase_user),
):
    url = URL + f"/{version}/connections/"
    uid = user["uid"]
    body = request_body.model_dump(exclude_unset=True)
    body["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@ConnectionsRouter.get("/{version}/connections/me")
async def get_my_connections(
    request: Request,
    version: str,
    request_query_params: GetUserConnections = Depends(),
    user=Depends(get_firebase_user),
):
    url = URL + f"/{version}/connections"
    uid = user["uid"]
    query_params = request_query_params.model_dump(exclude_none=True)
    query_params["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        params=query_params,
    )


@ConnectionsRouter.get("/{version}/connections/{connection_id}")
async def get_connection(
    request: Request,
    connection_id: str,
    version: str,
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/connections/{connection_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )


@ConnectionsRouter.get("/{version}/connections")
async def get_connections(
    request: Request,
    version: str,
    request_query_params: GetConnections = Depends(),
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/connections"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        params=request_query_params.model_dump(exclude_none=True),
    )


@ConnectionsRouter.patch("/{version}/connections/{connection_id}")
async def update_connection(
    request: Request,
    connection_id: str,
    request_body: UpdateConnection,
    version: str,
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/connections/{connection_id}"
    body = request_body.model_dump(exclude_unset=True)
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@ConnectionsRouter.delete("/{version}/connections/{connection_id}")
async def delete_connection(
    request: Request,
    connection_id: str,
    version: str,
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/connections/{connection_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )
