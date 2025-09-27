from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import os

def get_vectorstore():
    return Chroma(
        persist_directory="chroma_db",
        embedding_function=OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    )
