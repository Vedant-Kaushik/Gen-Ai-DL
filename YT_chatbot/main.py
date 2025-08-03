from youtube_transcript_api import YouTubeTranscriptApi
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from uuid import uuid4
import os
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

def get_video_id(url):
    return url.split("v=")[-1].split("&")[0] if "v=" in url else url.split("/")[-1]

# Example
# url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
# video_id = get_video_id(url)
# print("Video ID:", video_id)

def transcripter(id):
    
    ytt_api = YouTubeTranscriptApi()
    fetched_transcript = ytt_api.fetch(id, languages=['en','hi'])

    docs=[] 
    for snippet in fetched_transcript:
        docs.append(snippet.text)
    text = " ".join(doc.strip() for doc in docs )
    return text


#text=transcripter('S39b5laVmjs')

os.environ["GOOGLE_API_KEY"] = "AIzaSyCYxxxxxxxxx3ZbqhZCtL_Q"

embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def encoder(text):
    
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=1000,
        chunk_overlap=150,
        length_function=len,
    )
    chunked_texts = text_splitter.create_documents([text])

    vector_store = Chroma(
        collection_name="example_collection",
        embedding_function=embeddings,
    )
   
    uuids = [str(uuid4()) for _ in range(len(chunked_texts))]

    vector_store.add_documents(documents=chunked_texts, ids=uuids)
    return vector_store

# vector_store=encoder(text=transcripter('S39b5laVmjs'))

prompt = PromptTemplate(
    template='''
    
    You are an assistant that answers questions based on a YouTube video transcript.
    Only use the provided context chunks to answer the user's question.
    If the answer is not in the context, say "The video does not contain information about that."
    ---
    Context:
    {context}
    Question: {Question}
    Answer in a clear and concise way:''',
input_variables=['context', 'Question']
    )

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key="AIzaSyCxxxxxxxx3ZbqhZCtL_Q")

messages = [
        SystemMessage(content="You are a general-purpose language model that helps users with their queries. If the user greets you (e.g., says 'hi', 'hello', etc.), greet them warmly and politely in return. If the user tries to chat casually or go off-topic, acknowledge it briefly in a friendly way so you don’t seem rude, then gently redirect the conversation back to the main topic or context. Be helpful, conversational, and professional—but not overly robotic.")
    ]


def ask(question,vector_store, k=8, top_n=5, min_score=0.0):
    """Retrieve relevant context and get an answer from the model for a given question."""
    retriever = vector_store.similarity_search_with_score(question, k=k)
    context = "\n\n".join([doc.page_content for doc, _ in retriever[:5]])
    prompt_text = prompt.invoke({'context': context, 'Question': question}).text
    messages.append(SystemMessage(content=prompt_text))
    messages.append( HumanMessage(content=question))
    result = model.invoke(messages)
    messages.append(result)
    return result.content

# Example :
# answer = ask("where was he when he died")
# print(answer) 