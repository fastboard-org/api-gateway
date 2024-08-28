from fastapi import APIRouter
from configs.settings import settings
from request import make_request
from auth.firebase import get_firebase_user
from fastapi import Depends
from schemas.dashboards import (
    CreateDashboard,
    UpdateDashboard,
    GetDashboards,
)
from fastapi import Request

DashboardsRouter = APIRouter(tags=["dashboards"])

SERVICE_URL = settings.dashboards_service_url


@DashboardsRouter.post("/{version}/dashboards/{dashboard_id}/published")
async def publish_dashboard(
    request: Request,
    dashboard_id: str,
    version: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = SERVICE_URL + f"/{version}/dashboards/{dashboard_id}/published?user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )


@DashboardsRouter.post("/{version}/dashboards")
async def create_dashboard(
    request: Request,
    request_body: CreateDashboard,
    version: str,
    user=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/dashboards/"
    uid = user["uid"]
    body = request_body.model_dump(exclude_unset=True)
    body["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@DashboardsRouter.get("/{version}/dashboards/{dashboard_id}/published")
async def get_published_dashboard(
    request: Request,
    dashboard_id: str,
    version: str,
    _=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/dashboards/{dashboard_id}/published"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )


@DashboardsRouter.get("/{version}/dashboards/{dashboard_id}")
async def get_dashboard(
    request: Request,
    dashboard_id: str,
    version: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = SERVICE_URL + f"/{version}/dashboards/{dashboard_id}?user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )


@DashboardsRouter.get("/{version}/dashboards")
async def get_my_dashboards(
    request: Request,
    version: str,
    request_query_params: GetDashboards = Depends(),
    user=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/dashboards"
    uid = user["uid"]
    query_params = request_query_params.model_dump(exclude_none=True)
    query_params["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        params=query_params,
    )


@DashboardsRouter.patch("/{version}/dashboards/{dashboard_id}")
async def update_dashboard(
    request: Request,
    dashboard_id: str,
    version: str,
    request_body: UpdateDashboard,
    user=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/dashboards/{dashboard_id}"
    uid = user["uid"]
    body = request_body.model_dump(exclude_unset=True)
    body["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@DashboardsRouter.delete("/{version}/dashboards/{dashboard_id}")
async def delete_dashboard(
    request: Request,
    dashboard_id: str,
    version: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = SERVICE_URL + f"/{version}/dashboards/{dashboard_id}?user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )
