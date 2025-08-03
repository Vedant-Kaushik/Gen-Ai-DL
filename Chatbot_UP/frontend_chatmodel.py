import streamlit as st
from langchain.schema import HumanMessage, AIMessage
from backend_chatmodel import graph
st.title(" :blue[Chatbot]")
st.subheader("Built on :blue[LangGraph] ",divider=True)
# Initialize or retrieve session state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

for message in st.session_state['messages']:
    if isinstance(message, HumanMessage):
        role = "user"
        avatar = "🧑‍💻"  
    else:
        role = "AI"
        avatar = "🤖"  

    with st.chat_message(role, avatar=avatar):
        st.text(message.content)

# Input from user
user_input = st.chat_input("Say something")

# If input is received
if user_input:
    # Display user message
    with st.chat_message("user",avatar="🧑‍💻"):
        st.text(user_input)
    st.session_state['messages'].append(HumanMessage(content=user_input))

    # Build and invoke the workflow
    workflow = graph()
    config = {"configurable": {"thread_id": "1"}}
    state = {"messages": st.session_state['messages']}
    result = workflow.invoke(state, config=config)

    # Get AI response and display
    ai_response = result["messages"][-1].content
    st.session_state['messages'].append(AIMessage(content=ai_response))
    with st.chat_message("AI",avatar = "🤖"):
        st.text(ai_response)
