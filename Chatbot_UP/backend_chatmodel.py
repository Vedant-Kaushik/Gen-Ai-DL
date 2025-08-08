from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from dotenv import load_dotenv 

load_dotenv()
llm=ChatGoogleGenerativeAI(model='gemini-1.5-flash')

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

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
    checkpointer = InMemorySaver()
    workflow = graph.compile(checkpointer=checkpointer)
    return workflow


def chatting():
    workflow=graph()
    while True:
        textinput=input("ask anything = ")
        if textinput.strip().lower() in['bye','exit']:
            return 'Goodbye!  Have a great day.'
        initial_state = {
            'messages': [HumanMessage(content=textinput)]
        }
        config2 = {"configurable": {"thread_id": "2"}}
        
        ans=workflow.invoke(initial_state,config=config2)['messages'][-1].content
        #return ans
        print('AI:',ans)
        print(workflow.get_state(config=config2))


if __name__=="__main__":
    print(chatting())

chatbot = graph()
