# 🧠 PDF Knowledge Base with DeepSeek LLM

A fully local, offline knowledge system for querying PDFs using a local DeepSeek LLM and vector search.
Dockerized local PDF knowledge base with DeepSeek LLM, Gradio UI, FAISS vector search, and PDF snapshots.

## 🚀 Features
- Runs locally on Ubuntu via Docker
- Extracts text and page snapshots from PDFs
- Uses FAISS for semantic similarity search
- Runs DeepSeek LLM offline via oobabooga's text-generation-webui
- Simple Gradio UI with preview of related PDF pages

## 🧰 Requirements
- Docker + Docker Compose
- Local DeepSeek model files placed in `models/deepseek-llm/`
- Your documents placed in `data/`

## 🔧 Usage

```bash
git clone https://github.com/your-user/pdf-knowledge-base.git
cd pdf-knowledge-base
docker-compose up --build
