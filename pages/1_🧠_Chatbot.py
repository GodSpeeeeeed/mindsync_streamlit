import streamlit as st
from utils.chatbot import MentalHealthChatbot

st.set_page_config(
    page_title="MindSync Chat",
    page_icon="🧠"
)

st.title("🧠 MindSync Chatbot")
st.write("I'm here to listen and help. How are you feeling today?")

# Initialize chatbot
if 'chatbot' not in st.session_state:
    st.session_state.chatbot = MentalHealthChatbot()
    st.session_state.messages = []

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Type your message here..."):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Get chatbot response
    response = st.session_state.chatbot.get_response(prompt)
    
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)

# Add back button
if st.button("← Back to Home"):
    st.switch_page("app.py")