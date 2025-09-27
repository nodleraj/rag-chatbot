import os
import chromadb
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from ingestion import load_documents

def build_vectorstore():
    documents = load_documents()
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = Chroma.from_documents(documents, embeddings, persist_directory="chroma_db")
    vectorstore.persist()
    return vectorstore
