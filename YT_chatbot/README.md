# YouTube Transcript Chatbot Backend

A FastAPI backend for a chatbot that answers questions about the transcript of any YouTube video. The backend dynamically fetches the transcript, builds a vector store for semantic search, and answers user questions using an LLM (Google Gemini).

## Features

- Accepts a YouTube video URL and a user question via API
- Dynamically fetches and processes the transcript for each video
- Caches vector stores per video for fast repeated queries (with automatic expiry)
- Uses Google Generative AI for embeddings and chat
- No frontend included—API is ready for integration with any client (web, mobile, etc.)

## Setup Instructions

### 1. Clone the repository and install dependencies

```sh
pip install -r requirements.txt
pip install cachetools python-dotenv fastapi uvicorn youtube-transcript-api langchain-google-genai langchain-chroma
```

### 2. Create a `.env` file in the project root

```
GOOGLE_API_KEY=your_actual_google_api_key_here
```

### 3. Run the FastAPI backend

```sh
uvicorn YT_chatbot.backend_fastAPI:app --reload
```

The API will be available at `http://127.0.0.1:8000` and interactive docs at `http://127.0.0.1:8000/docs`.

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

- The backend will extract the video ID from the URL, fetch and process the transcript, and answer the question.
- The vector store for each video is cached for 1 hour or up to 10 videos (configurable).

## Notes

- **No frontend is included.** You can build your own UI or integrate with any client.
- **API keys:** Never commit your `.env` file or API keys to public repositories.
- **Caching:** Uses an in-memory TTL cache for vector stores. For production, consider a distributed cache if running multiple backend instances.
- **Error handling:** If YouTube blocks transcript requests, see the [youtube-transcript-api README](https://github.com/jdepoix/youtube-transcript-api#working-around-ip-bans-requestblocked-or-ipblocked-exception) for workarounds.

## License

MIT
