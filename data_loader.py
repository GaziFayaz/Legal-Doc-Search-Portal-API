from pathlib import Path
import json
from fastapi import HTTPException


def get_documents():
    try:
        DATA_FILE = Path(__file__).parent / "data" / "mock_documents.json"
        with open(DATA_FILE) as f:
            documents = json.load(f)
        return documents
    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Error loading documents data",
        )
