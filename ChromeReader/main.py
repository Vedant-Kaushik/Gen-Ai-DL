from langchain_community.document_loaders import ScrapingAntLoader
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=os.environ["GOOGLE_API_KEY"])

prompt = PromptTemplate(
        template=(
            "Extracted info:\n{text}\n\n"
            "Question: {question}\n\n"
            
        ),
        input_variables=['question', 'text']
        )

parser = StrOutputParser()
chain = prompt | model | parser

messages = [
    SystemMessage(content=
        """You are a general-purpose language model that helps users with their queries.
If the user greets you (e.g., says "hi", "hello", etc.), greet them warmly and politely in return.If the user tries to chat casually or go off-topic, acknowledge it briefly in a friendly way so you don’t seem rude, then gently redirect the conversation back to the main topic or context.
Be helpful, conversational, and professional—but not overly robotic."""
    )
]
if __name__ == '__main__':
    url = 'https://medium.com/data-science-collective/stock-price-prediction-using-machine-learning-in-python-4fb314565abd'
    loader = ScrapingAntLoader([url], api_key=os.environ["SCRAPING_ANT_API_KEY"])
    docs = loader.load()
    while True:
        user_question = input('Enter your question: ')
        if user_question.lower() == 'exit':
            break
        messages.append(HumanMessage(content=user_question))
        page_content = docs[0].page_content
        answer = chain.invoke({'question': messages, 'text': page_content})
        messages.append(AIMessage(content=answer))
        print(answer)