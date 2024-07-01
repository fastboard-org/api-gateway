from fastapi import APIRouter
from configs.settings import settings
from request import make_request
from auth.firebase import get_firebase_user
from fastapi import Depends, Request
from schemas.queries import CreateQuery, UpdateQuery, GetQueries, GetUserQueries

QueriesRouter = APIRouter(tags=["queries"])

URL = settings.dashboards_service_url


@QueriesRouter.post("/{version}/queries")
async def create_query(
    request: Request,
    request_body: CreateQuery,
    version: str,
    user=Depends(get_firebase_user),
):
    url = URL + f"/{version}/queries"
    uid = user["uid"]
    body = request_body.model_dump(exclude_unset=True)
    body["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@QueriesRouter.get("/{version}/queries/me")
async def get_my_queries(
    request: Request,
    version: str,
    request_query_params: GetUserQueries = Depends(),
    user=Depends(get_firebase_user),
):
    url = URL + f"/{version}/queries"
    uid = user["uid"]
    query_params = request_query_params.model_dump(exclude_none=True)
    query_params["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        params=query_params,
    )


@QueriesRouter.get("/{version}/queries/{query_id}")
async def get_query(
    request: Request,
    query_id: str,
    version: str,
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/queries/{query_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )


@QueriesRouter.get("/{version}/queries")
async def get_queries(
    request: Request,
    version: str,
    request_query_params: GetQueries = Depends(),
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/queries"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        params=request_query_params.model_dump(exclude_none=True),
    )


@QueriesRouter.patch("/{version}/queries/{query_id}")
async def update_query(
    request: Request,
    query_id: str,
    request_body: UpdateQuery,
    version: str,
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/queries/{query_id}"
    body = request_body.model_dump(exclude_unset=True)
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@QueriesRouter.delete("/{version}/queries/{query_id}")
async def delete_query(
    request: Request,
    query_id: str,
    version: str,
    _=Depends(get_firebase_user),
):
    url = URL + f"/{version}/queries/{query_id}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )
