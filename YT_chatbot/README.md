# YouTube Transcript Chatbot

A modular, production-ready system for answering questions about the transcript of any YouTube video. This project combines transcript fetching, semantic chunking, vector search, and LLM-powered answers, all accessible via a FastAPI backend. Designed for easy integration and extensibility.

---

## Project Overview

This chatbot lets you ask questions about the content of any YouTube video. It fetches the transcript, splits it into meaningful chunks, creates vector embeddings, and uses a large language model (LLM) to answer your questions based on the video content.

---

## Architecture

- **Transcript Fetcher:** Downloads video transcripts using `youtube-transcript-api`.
- **Encoder/Vector Store:** Splits transcripts into chunks and encodes them for semantic search (using Chroma and Google Generative AI embeddings).
- **Retriever:** Finds the most relevant transcript chunks for a given question.
- **LLM:** Answers questions using the retrieved context (Google Gemini or similar).
- **Caching:** Caches vector stores per video for fast repeated queries (with automatic expiry).
- **API Layer:** FastAPI backend exposes the chatbot as a simple API.

---

## Features

- Dynamic transcript fetching for any YouTube video
- Semantic chunking and vector search for accurate retrieval
- LLM-powered answers based on video content
- Caching for efficiency (per-video, with expiry)
- API endpoint for easy integration

---

## File/Module Structure

- `main.py` — Core logic: transcript fetching, chunking, encoding, retrieval, and answer generation
- `backend_fastAPI.py` — FastAPI backend: exposes the chatbot as an API, manages per-video caching
- `requirements.txt` — All dependencies needed to run the project
- `README.md` — Project documentation

---

## Setup Instructions

### 1. Install dependencies

```sh
pip install -r requirements.txt
```

### 2. Set up your Google API key

**IMPORTANT:**

- You must use your own Google API key for Generative AI.
- **Do NOT use any example key in the code.**
- Set your key as an environment variable before running:

```sh
export GOOGLE_API_KEY=your_actual_google_api_key_here
```

Or add it to a `.env` file if you use `python-dotenv`.

### 3. Run the FastAPI backend

```sh
uvicorn backend_fastAPI:app --reload
```

The API will be available at `http://127.0.0.1:8000` and interactive docs at `http://127.0.0.1:8000/docs`.

---

## API Usage Example

**POST** `/chatbot`

**Request JSON:**

```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "Question": "What is this video about?"
}
```

**Response JSON:**

```json
{
  "answer": "..."
}
```

- The backend extracts the video ID, fetches and processes the transcript, and answers the question.
- Vector stores are cached per video for 1 hour or up to 10 videos (configurable).

---

## Extensibility & Customization

- Swap out the LLM or embedding model as needed (see `main.py`)
- Adjust chunking, retrieval, or caching logic for your use case
- Integrate with any frontend or client (web, mobile, etc.)

---

## License

MIT

---

## Credits

- Built using FastAPI, Chroma, LangChain, Google Generative AI, and youtube-transcript-api.
- Special thanks to open-source contributors and the AI/ML community.
