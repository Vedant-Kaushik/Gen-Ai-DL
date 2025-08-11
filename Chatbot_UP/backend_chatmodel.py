from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from dotenv import load_dotenv 
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3

load_dotenv()
llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

conn = sqlite3.connect(database="checkpoints.db", check_same_thread=False)
checkpointer = SqliteSaver(conn)

def retrieve_all_threads():
    all_threads = set()
    for checkpoint in checkpointer. list(None):
        all_threads.add (checkpoint.config['configurable']['thread_id'])
    return list(all_threads)

def chat_node(state: ChatState):

    # take user query from state
    messages = state['messages']

    # send to llm
    response = llm.invoke(messages)

    # response store state
    return {'messages': [response]}

def graph():
    graph = StateGraph(ChatState)

    # add nodes
    graph.add_node('chat_node', chat_node)

    graph.add_edge(START, 'chat_node')
    graph.add_edge('chat_node', END)
    
    workflow = graph.compile(checkpointer=checkpointer)
    return workflow


def chatting():
    workflow=graph()
    
    textinput=input("ask somehting = ")
    if textinput.strip().lower() in['bye','exit']:
        return 'Goodbye!  Have a great day.'
    initial_state = {
        'messages': [HumanMessage(content=textinput)]
    }
    config2 = {"configurable": {"thread_id": "therad-1"}}
    
    ans=workflow.invoke(initial_state,config=config2)['messages'][-1].content
    return ans
    #print('AI:',ans)


if __name__=="__main__":
    print(chatting())

chatbot=graph()


