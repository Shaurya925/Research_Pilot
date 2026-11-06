
# ResearchPilot 📚

**ResearchPilot** is an AI-powered research assistant that allows users to upload PDF documents and ask questions about their content. It uses Retrieval-Augmented Generation (RAG), hybrid retrieval, and Cross-Encoder reranking to generate relevant, document-grounded answers.

**Current Status:** Working Streamlit chatbot with PDF question answering, hybrid retrieval, reranking, and page-level source references.

## 🚀 Features

- **PDF Ingestion:** Loads PDF documents using PyMuPDF.
- **Text Chunking:** Splits documents into overlapping chunks using RecursiveCharacterTextSplitter.
- **Embeddings:** Uses `sentence-transformers/all-MiniLM-L6-v2`.
- **Vector Search:** FAISS for semantic retrieval with Maximal Marginal Relevance (MMR).
- **Keyword Search:** BM25 for exact keyword-based retrieval.
- **Hybrid Retrieval:** Combines FAISS and BM25 using EnsembleRetriever.
- **Reranking:** Uses BAAI's `bge-reranker-base` Cross-Encoder to improve retrieval relevance.
- **LLM Integration:** Uses Groq-hosted LLMs for answer generation.
- **Source References:** Extracts PDF source names and page numbers from document metadata.
- **Chat Interface:** Interactive Streamlit application.
- **Resource Caching:** Caches the retriever and LLM to avoid unnecessary initialization.

## 🏗️ Architecture

```text
              PDF Upload
                  |
                  v
             PDF Loading
               PyMuPDF
                  |
                  v
             Text Chunking
                  |
          +-------+-------+
          |               |
          v               v
    FAISS Retrieval    BM25 Retrieval
    (Semantic Search)  (Keyword Search)
          |               |
          +-------+-------+
                  |
                  v
            Hybrid Retrieval
          (EnsembleRetriever)
                  |
                  v
          Cross-Encoder Reranking
             (BGE Reranker)
                  |
                  v
          Top Relevant Chunks
                  |
                  v
             Groq LLM
                  |
                  v
          Generated Answer
                  |
                  v
          Source References
```

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| PDF Processing | PyMuPDF |
| Framework | LangChain |
| Text Chunking | RecursiveCharacterTextSplitter |
| Embeddings | Hugging Face |
| Vector Database | FAISS |
| Keyword Retrieval | BM25 |
| Hybrid Retrieval | EnsembleRetriever |
| Reranking | Cross-Encoder |
| LLM | Groq |
| Frontend | Streamlit |
| Dependency Management | uv |

## 📂 Project Structure

```text
ResearchPilot/
│
├── documents/
│   └── sample.pdf
│
├── src/
│   ├── app.py
│   ├── rag.py
│   ├── retriver.py
│   ├── reranker.py
│   └── llm.py
│
├── .env
├── .gitignore
├── pyproject.toml
├── uv.lock
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ResearchPilot.git

cd ResearchPilot
```

### 2. Install dependencies

Make sure you have Python and uv installed.

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

Never commit your API key to GitHub.

### 4. Run the application

```bash
uv run streamlit run src/app.py
```

Open the local URL provided by Streamlit.

Upload a PDF and start asking questions!

## 🧠 Retrieval Pipeline

ResearchPilot uses a combination of two retrieval techniques:

**1. Dense Retrieval (FAISS)**

Uses Hugging Face embeddings to retrieve semantically relevant document chunks. MMR helps improve diversity among retrieved results.

**2. Sparse Retrieval (BM25)**

Uses keyword matching to identify chunks containing relevant terms.

**3. Hybrid Retrieval**

Combines the results of FAISS and BM25 through EnsembleRetriever using Reciprocal Rank Fusion.

**4. Reranking**

Uses a Cross-Encoder model (`BAAI/bge-reranker-base`) to score question-document pairs and reorder retrieved chunks according to relevance.

## 📌 Current Limitations

The following features are not yet implemented:

- Conversational memory for context-aware follow-up questions.
- Multiple PDF uploads and cross-document retrieval.
- Streaming LLM responses.
- Formal retrieval and answer evaluation.
- Public deployment.

## 🗺️ Future Roadmap

The next development phases are:

- [ ] Conversational Memory
- [ ] Multiple PDF Support
- [ ] Streaming Responses
- [ ] RAG Evaluation using RAGAS / DeepEval
- [ ] Deployment

## 🎯 Project Goal

The goal of ResearchPilot is to build a reliable AI research assistant capable of understanding technical documents and research papers, retrieving relevant information, maintaining conversational context, and generating accurate answers grounded in source documents.

---

**ResearchPilot — Making research smarter with AI.**
