from pydantic import BaseModel
from typing import Optional


class CreateDashboard(BaseModel):
    name: str
    folder_id: Optional[str] = None
    metadata: dict


class UpdateDashboard(BaseModel):
    name: Optional[str] = None
    folder_id: Optional[str] = None
    metadata: Optional[dict] = None


class GetDashboards(BaseModel):
    folder_id: Optional[str] = None
    name: Optional[str] = None
