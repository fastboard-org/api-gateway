from pydantic import BaseModel
from typing import Optional


class CreateFolder(BaseModel):
    name: str


class UpdateFolder(BaseModel):
    name: Optional[str] = None


class GetFolders(BaseModel):
    name: Optional[str] = None
