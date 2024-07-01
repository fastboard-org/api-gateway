from pydantic import BaseModel
from typing import Optional


class CreateQuery(BaseModel):
    name: str
    connection_id: str
    metadata: dict


class UpdateQuery(BaseModel):
    name: Optional[str] = None
    metadata: Optional[dict] = None


class GetQueries(BaseModel):
    user_id: Optional[str] = None
    connection_id: Optional[str] = None
    name: Optional[str] = None


class GetUserQueries(BaseModel):
    connection_id: Optional[str] = None
    name: Optional[str] = None
