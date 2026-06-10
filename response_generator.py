import random
from data_loader import get_documents
from match_documents import get_matching_documents
from models import Data


def generate_response(query: str) -> Data:
    matches = get_matching_documents(query)

    if not matches:
        documents = get_documents()
        document = documents[random.randint(0, len(documents) - 1)]
        return Data(
            title=document["title"],
            content=document["content"],
            summary=document["summary"],
        )

    top_doc = matches[0]

    return Data(
        title=top_doc["title"], content=top_doc["content"], summary=top_doc["summary"]
    )
