from pydantic import BaseModel
from typing import Optional


class CreateConnection(BaseModel):
    name: str
    type: str
    credentials: dict
    variables: dict


class UpdateConnection(BaseModel):
    name: Optional[str] = None
    credentials: Optional[dict] = None
    variables: Optional[dict] = None


class GetConnections(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
