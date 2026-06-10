from datetime import datetime

from fastapi import FastAPI, HTTPException
from fastapi.requests import Request as FastAPIRequest
from fastapi.responses import JSONResponse
from models import ErrorResponse, Request, Response
from response_generator import generate_response

app = FastAPI()


@app.exception_handler(HTTPException)
async def http_exception_handler(
    request: FastAPIRequest, exc: HTTPException
) -> JSONResponse:
    error = ErrorResponse(
        success=False,
        statusCode=exc.status_code,
        message=str(exc.detail),
    )
    return JSONResponse(
        status_code=exc.status_code,
        content=error.model_dump(),
        headers=exc.headers,
    )


@app.get("/")
def read_root():
    return {"Server": "Running", "Timestamp": f"{datetime.now()}"}


@app.post("/generate", response_model=Response)
def generate(request: Request):
    response = generate_response(request.query)
    return Response(
        success=True,
        statusCode=200,
        message="Document generated successfully",
        data=response,
    )
