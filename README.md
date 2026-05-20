# Dialogflow CX RAG Chatbot

A fully local, private RAG (Retrieval Augmented Generation) chatbot built with LlamaIndex and Ollama. Chat with Dialogflow CX documentation without sending any data to the cloud.

## Tech Stack
- **LlamaIndex** - RAG pipeline and document indexing
- **Ollama** - Local LLM serving
- **Llama 3** - Language model for generating answers
- **nomic-embed-text** - Fast local embeddings
- **Python** - Core language

## How it works
1. Loads PDF documents into a vector index
2. When you ask a question, it retrieves the most relevant chunks from your docs
3. Passes those chunks to Llama 3 to generate a grounded answer
4. Everything runs locally — no API keys, no data logging

## Setup
1. Install [Ollama](https://ollama.com) and pull the required models:
```bash
   ollama pull llama3
   ollama pull nomic-embed-text
```
2. Clone the repo and create a virtual environment:
```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama
```
3. Add your PDFs to the `data/` folder
4. Run it:
```bash
   python3 rag.py
```

## Why local?
Privacy. No conversations logged, no data used for training, no API costs.