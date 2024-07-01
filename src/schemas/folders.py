from pydantic import BaseModel
from typing import Optional


class CreateFolder(BaseModel):
    name: str


class UpdateFolder(BaseModel):
    name: Optional[str] = None


class GetFolders(BaseModel):
    user_id: Optional[str] = None
    name: Optional[str] = None


class GetUserFolders(BaseModel):
    name: Optional[str] = None
