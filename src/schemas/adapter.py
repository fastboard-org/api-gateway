from pydantic import BaseModel
from typing import Union


class ExecuteQuery(BaseModel):
    parameters: dict


class ApiMetadata(BaseModel):
    method: str
    path: str
    headers: dict
    body: dict


class MongoMetadata(BaseModel):
    method: str
    collection: str
    filter_body: Union[dict, list, str]
    update_body: Union[dict, list, str]


class PreviewQuery(BaseModel):
    parameters: dict
    connection_metadata: Union[ApiMetadata, MongoMetadata]
