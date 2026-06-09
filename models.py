# request response models
from pydantic import BaseModel

class Request(BaseModel):
  query: str
 
class Response(BaseModel):
  statusCode: int
  status: str
  message: str
  data: dict[str, str] | None = None
  
class ErrorResponse(BaseModel):
  statusCode: int
  status: str
  message: str