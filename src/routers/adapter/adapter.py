from fastapi import APIRouter
from configs.settings import settings
from request import make_request
from fastapi import Depends, Request
from schemas.adapter import ExecuteQuery, PreviewQuery
from auth.firebase import get_firebase_user

AdapterRouter = APIRouter(tags=["adapter"])

URL = settings.adapter_service_url


@AdapterRouter.post("/{version}/adapter/{connection_id}/execute/{query_id}")
async def execute_query(
    request: Request,
    request_body: ExecuteQuery,
    version: str,
    connection_id: str,
    query_id: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = URL + f"/{version}/adapter/{connection_id}/execute/{query_id}?user_id={uid}"
    body = request_body.model_dump()
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@AdapterRouter.post("/{version}/adapter/{connection_id}/preview")
async def preview_query(
    request: Request,
    request_body: PreviewQuery,
    version: str,
    connection_id: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = URL + f"/{version}/adapter/{connection_id}/preview?user_id={uid}"
    body = request_body.model_dump()
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )
