from fastapi import FastAPI
from rag_pipeline import get_rag_chain

app = FastAPI()
qa = get_rag_chain()

@app.get("/ask")
def ask(query: str):
    return {"answer": qa.run(query)}

@app.get("/health")
def health():
    return {"status": "ok"}
