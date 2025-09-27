# RAG Chatbot

## Setup
```bash
python3 -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file with:
```
OPENAI_API_KEY=your_api_key_here
```

## Build Vector Store
```bash
python3 src/embeddings.py
```

## Run CLI chatbot
```bash
python3 src/rag_pipeline.py
```

## Run API
```bash
uvicorn src.api:app --reload
```
Visit: http://127.0.0.1:8000/ask?query=Hello
