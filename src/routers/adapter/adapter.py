from fastapi import APIRouter
from configs.settings import settings
from request import make_request
from fastapi import Request
from schemas.adapter import ExecuteQuery, PreviewQuery

AdapterRouter = APIRouter(tags=["adapter"])

URL = settings.adapter_service_url


@AdapterRouter.post("/{version}/embeddings/{query_id}")
async def create_embeddings(
    request: Request, version: str, query_id: str, index_field: str
):
    url = URL + f"/{version}/adapter/embeddings/{query_id}?index_field={index_field}"
    return await make_request(url, dict(request.headers), request.method)


@AdapterRouter.post("/{version}/adapter/execute/{query_id}")
async def execute_query(
    request: Request,
    request_body: ExecuteQuery,
    version: str,
    query_id: str,
):
    url = URL + f"/{version}/adapter/execute/{query_id}"
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
):
    url = URL + f"/{version}/adapter/{connection_id}/preview"
    body = request_body.model_dump()
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )
