from reranker import rerank_documents



from reranker import rerank_documents


def answer_question(retriever, llm, question: str):

    # Hybrid retrieval
    documents = retriever.invoke(question)

    # Reranking
    documents = rerank_documents(
        question=question,
        documents=documents,
        top_k=4
    )

    # Collect citations
    citations = set()

    for doc in documents:
        page = doc.metadata.get("page")
        source = doc.metadata.get("source")

        if page is not None:
            citations.add((source, page + 1))

    # Build context
    context = "\n\n".join(
        doc.page_content for doc in documents
    )

    prompt = f"""
    Answer the question using only the context below.

    If the answer is not present in the context,
    say that you cannot find the answer in the document.

    Context:
    {context}

    Question:
    {question}
    """

    response = llm.invoke(prompt)

    return response.content, sorted(citations)
