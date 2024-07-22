from pydantic import BaseModel


class ExecuteQuery(BaseModel):
    parameters: dict


class PreviewQuery(BaseModel):
    parameters: dict
    method: str
    path: str
    headers: dict
    body: dict
