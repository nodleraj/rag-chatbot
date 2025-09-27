from retrieval import get_vectorstore
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI
import os

def get_rag_chain():
    vectorstore = get_vectorstore()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", openai_api_key=os.getenv("OPENAI_API_KEY"))
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa

if __name__ == "__main__":
    qa = get_rag_chain()
    while True:
        query = input("Ask me something: ")
        if query.lower() in ["exit", "quit"]:
            break
        print(qa.run(query))
