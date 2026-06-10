# request response models
from pydantic import BaseModel


class Data(BaseModel):
    title: str
    content: str
    summary: str


class Request(BaseModel):
    query: str


class Response(BaseModel):
    success: bool
    statusCode: int
    message: str
    data: Data | None = None


class ErrorResponse(BaseModel):
    success: bool
    statusCode: int
    message: str
