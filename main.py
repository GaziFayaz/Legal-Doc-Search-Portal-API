from datetime import datetime

from fastapi import FastAPI
from models import Request, Response

app = FastAPI()

@app.get("/")
def read_root():
    return {"Server": "Running","Timestamp": f"{datetime.now()}"}

@app.post("/generate", response_model=Response)
def generate(request: Request):
    return Response(
        statusCode=200,
        status="success",
        message="Document generated successfully",
        data={"generated_document": f"Generated document for query: {request.query}"}
    )