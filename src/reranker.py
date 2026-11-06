
from sentence_transformers import CrossEncoder

MODEL_NAME = "BAAI/bge-reranker-base"

reranker = CrossEncoder(MODEL_NAME)


def rerank_documents(question: str, documents: list, top_k: int = 4):
    pairs = [
        [question, doc.page_content]
        for doc in documents
    ]

    scores = reranker.predict(pairs)

    ranked_documents = sorted(
        zip(documents, scores),
        key=lambda item: item[1],
        reverse=True
    )

    return [
        doc for doc, score in ranked_documents[:top_k]
    ]
