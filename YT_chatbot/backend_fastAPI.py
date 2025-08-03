from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Annotated
from YT_chatbot.main import transcripter, encoder, ask,get_video_id
from cachetools import TTLCache

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class UserInput(BaseModel):
    Question: Annotated[str, Field(..., description='question you want to ask')]
    url: Annotated[str, Field(..., description='YouTube video url')]

# Each entry expires after 1 hour, up to 10 videos cached
vector_cache = TTLCache(maxsize=10, ttl=3600)

@app.post('/chatbot')
def predict_answer(data: UserInput):
    video_id = get_video_id(data.url)
    # Check if vector store for this video is already cached
    if video_id not in vector_cache:
        # Build and cache for this video
        text = transcripter(video_id)
        vector_store = encoder(text)
        vector_cache[video_id] = vector_store
       
    else:
        vector_store = vector_cache[video_id]
   
    answer = ask(data.Question,vector_store)
    return JSONResponse(status_code=200, content={'answer': answer,'error':'Transcript not available for this video'})




