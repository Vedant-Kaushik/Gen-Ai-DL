import streamlit as st
import backend_chatmodel as backend
from langchain_core.messages import HumanMessage
import uuid

# *********************************** Utility Functions ***********************************

def generate_thread_id():
    return str(uuid.uuid4())

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state['thread_id'] = thread_id
    add_thread(thread_id)
    st.session_state['message_history'] = []

def add_thread(thread_id):
    if thread_id not in st.session_state['chat_threads']:
        st.session_state['chat_threads'].append(thread_id)

def load_conversation(thread_id):
    try:
        messages = backend.chatbot.get_state(config={'configurable': {'thread_id': thread_id}}).values['messages']
        temp_messages = []
        for msg in messages:
            role = 'user' if isinstance(msg, HumanMessage) else 'assistant'
            temp_messages.append({'role': role, 'content': msg.content})
        return temp_messages
    except Exception as e:
        return []


# *********************************** Session State Setup ***********************************

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if 'thread_id' not in st.session_state:
    st.session_state['thread_id'] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = []

add_thread(st.session_state['thread_id'])


# *********************************** Sidebar UI ***********************************

st.sidebar.title('LangGraph Chatbot')

if st.sidebar.button('New Chat'):
    reset_chat()

st.sidebar.header('My Conversations')

for thread_id in st.session_state['chat_threads'][::-1]:
    if st.sidebar.button(str(thread_id)):
        st.session_state['thread_id'] = thread_id
        st.session_state['message_history'] = load_conversation(thread_id)


# *********************************** Main UI ***********************************

st.title("Chatbot\nBuilt on LangGraph")

# Display message history
if not st.session_state['message_history']:
    st.markdown("**No messages to display.**")
else:
    for message in st.session_state['message_history']:
        with st.chat_message(message['role']):
            st.text(message['content'])

# Input box
user_input = st.chat_input("Type here...")

if user_input:
    # Show user message immediately
    st.session_state['message_history'].append({'role': 'user', 'content': user_input})
    with st.chat_message("user"):
        st.text(user_input)

    # Call LangGraph backend
    CONFIG = {'configurable': {'thread_id': st.session_state['thread_id']}}
    with st.chat_message("assistant"):
        ai_response = st.write_stream(
            chunk.content for chunk, _ in backend.chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages"
            )
        )

    # Append AI response
    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_response})