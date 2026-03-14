import streamlit as st
from streamlit_autorefresh import st_autorefresh  # type: ignore

from src.client.client import ChatClient
from components import chat_message

'''
# ChatBox

This is a simple Streamlit application that connects to a WebSocket server to send and receive messages in real-time. 
The application allows users to input messages, which are sent to the server, and displays incoming messages from the server.
'''

st_autorefresh(interval=1000)

if 'messages' not in st.session_state:
    st.session_state.messages = []


# Instantiate the client (persist in session state to avoid recreating on each rerun)
if 'client' not in st.session_state:
    client = ChatClient()
    st.session_state.client = client

client = st.session_state.client
for msg in client.get_messages():
    st.session_state.messages.append({'author': msg.user, 'msg': msg.content})

st.title("Real-Time WebSocket Client")

# Username input
username = st.text_input("Enter your username", key="username", disabled=st.session_state.get('connected', False))

button_text = "Disconnect" if st.session_state.get('connected', False) else "Connect"
disabled = not username.strip()  # Disable if username is empty or whitespace
if st.button(button_text, disabled=disabled):
    if st.session_state.get('connected', False):
        client.disconnect()
        st.session_state.connected = False
    else:
        client.connect(username)
        st.session_state.connected = True

# Handle sending messages
new_msg = st.chat_input("Enter message")
if new_msg:
    client.send_message(new_msg)
    st.session_state.messages.append({'author': st.session_state.username, 'msg': new_msg})

# Display messages in a scrollable container with two columns
with st.container(height=400):
    for msg in st.session_state.messages:
        if msg['author'] == username:
            chat_message(msg["msg"], "You", "10:30 AM", sent_by_me=True)
        else:
            chat_message(msg["msg"], msg['author'], "10:30 AM", sent_by_me=False)
