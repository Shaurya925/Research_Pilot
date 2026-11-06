
import streamlit as st
import tempfile
import hashlib
from pathlib import Path

from retriver import build_retriver
from llm import load_llm
from rag import answer_question


st.set_page_config(
    page_title="ResearchPilot",
    page_icon="📚",
    layout="centered"
)


@st.cache_resource
def load_components(pdf_bytes):

    file_hash = hashlib.sha256(pdf_bytes).hexdigest()

    pdf_path = Path(tempfile.gettempdir()) / f"{file_hash}.pdf"
    pdf_path.write_bytes(pdf_bytes)

    retriever = build_retriver(str(pdf_path))
    llm = load_llm()

    return retriever, llm


st.title("📚 ResearchPilot")
st.caption("Your AI-powered PDF research assistant")

uploaded_file = st.file_uploader(
    "Upload your research PDF",
    type=["pdf"]
)


if uploaded_file:

    pdf_bytes = uploaded_file.getvalue()

    current_hash = hashlib.sha256(pdf_bytes).hexdigest()

    if st.session_state.get("pdf_hash") != current_hash:
        st.session_state.pdf_hash = current_hash
        st.session_state.messages = []

    st.success(f"Loaded: {uploaded_file.name}")

    with st.spinner("Preparing your research assistant..."):
        retriever, llm = load_components(pdf_bytes)

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.markdown(message["content"])

            if message.get("citations"):
                st.caption("Sources:")
                for source, page in message["citations"]:
                    st.caption(f"📄 {Path(source).name} — Page {page}")

    question = st.chat_input("Ask something about your PDF...")

    if question:

        st.session_state.messages.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            with st.spinner("ResearchPilot is thinking..."):

                answer, citations = answer_question(
                    retriever,
                    llm,
                    question
                )

            st.markdown(answer)

            if citations:
                st.markdown("**Sources**")
                for source, page in citations:
                    st.caption(
                        f"📄 {Path(source).name} — Page {page}"
                    )

        st.session_state.messages.append({
            "role": "assistant",
            "content": answer,
            "citations": citations
        })

else:
    st.info("Upload a PDF to start chatting with ResearchPilot.")
