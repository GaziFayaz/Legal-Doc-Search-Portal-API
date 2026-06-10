from data_loader import get_documents


def get_matching_documents(query: str):
    query_keywords = query.lower().split()
    documents = get_documents()
    scored_docs = []

    for doc in documents:
        score = 0
        doc_content_words = doc["content"].lower().split()
        for keyword in query_keywords:
            score += doc_content_words.count(keyword)

        if score > 0:
            scored_docs.append({**doc, "score": score})

    scored_docs.sort(key=lambda doc: doc["score"], reverse=True)

    return scored_docs
