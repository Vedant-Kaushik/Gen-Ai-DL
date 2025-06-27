from fastapi import FastAPI
from pydantic import BaseModel,Field
from fastapi.responses import JSONResponse
from webpagereader.ChromeReader.main import chain,messages
from langchain_community.document_loaders import ScrapingAntLoader
import os
from fastapi.middleware.cors import CORSMiddleware
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class URLRequest(BaseModel):
    url: str=Field(...,description="The URL of the website to scrape",example="https://www.example.com")
    Question:str=Field(...,description="The question to ask the website",example="What is the main content of the page?")

@app.post("/scrape")
def scrape(request: URLRequest):
    while True:
        if request.Question.lower() == "exit":
            break
        try:
            messages.append(HumanMessage(content=request.Question))
            loader = ScrapingAntLoader([request.url], api_key=os.environ["SCRAPING_ANT_API_KEY"])
            docs = loader.load()
            if not docs:
                return JSONResponse(status_code=404, content={"answer": "Could not load the web page."})
            page_content = docs[0].page_content
            answer = chain.invoke({'question': messages, 'text': page_content})
            messages.append(AIMessage(content=answer))
            return JSONResponse(status_code=200,content={"answer": answer})
        except Exception as e:
            return JSONResponse(status_code=500, content={"answer": f"Error: {str(e)}"})
    