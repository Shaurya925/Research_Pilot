from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def load_llm():
    llm = ChatGroq(
        model="openai/gpt-oss-20b",
        temperature=0.2
    )

    return llm

