from fastapi import APIRouter
from configs.settings import settings
from request import make_request
from auth.firebase import get_firebase_user
from fastapi import Depends, Request
from schemas.folders import CreateFolder, UpdateFolder, GetFolders


FoldersRouter = APIRouter(tags=["folders"])


SERVICE_URL = settings.dashboards_service_url


@FoldersRouter.post("/{version}/folders")
async def create_folder(
    request: Request,
    request_body: CreateFolder,
    version: str,
    user=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/folders/"
    uid = user["uid"]
    body = request_body.model_dump(exclude_unset=True)
    body["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@FoldersRouter.get("/{version}/folders/{folder_id}")
async def get_folder(
    request: Request,
    folder_id: str,
    version: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = SERVICE_URL + f"/{version}/folders/{folder_id}?user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )


@FoldersRouter.get("/{version}/folders")
async def get_my_folders(
    request: Request,
    version: str,
    request_query_params: GetFolders = Depends(),
    user=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/folders"
    uid = user["uid"]
    query_params = request_query_params.model_dump(exclude_none=True)
    query_params["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        params=query_params,
    )


@FoldersRouter.patch("/{version}/folders/{folder_id}")
async def update_folder(
    request: Request,
    folder_id: str,
    request_body: UpdateFolder,
    version: str,
    user=Depends(get_firebase_user),
):
    url = SERVICE_URL + f"/{version}/folders/{folder_id}"
    uid = user["uid"]
    body = request_body.model_dump(exclude_unset=True)
    body["user_id"] = uid
    return await make_request(
        url,
        dict(request.headers),
        request.method,
        body=body,
    )


@FoldersRouter.delete("/{version}/folders/{folder_id}")
async def delete_folder(
    request: Request,
    folder_id: str,
    version: str,
    user=Depends(get_firebase_user),
):
    uid = user["uid"]
    url = SERVICE_URL + f"/{version}/folders/{folder_id}?user_id={uid}"
    return await make_request(
        url,
        dict(request.headers),
        request.method,
    )
