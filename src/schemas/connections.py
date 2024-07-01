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
    user_id: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None


class GetUserConnections(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
