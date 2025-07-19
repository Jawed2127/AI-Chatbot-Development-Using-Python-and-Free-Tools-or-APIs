import streamlit as st
import sys
import os

# Add backend path
sys.path.append(os.path.join(os.getcwd(), "Backend"))
from Chatbot import ChatBot
from SpeechToText import SpeechRecognition

# ---- Page Config ----
st.set_page_config(page_title="AiChatBot", layout="wide")

# ---- Custom Styling ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    background-color: #f0f2f6;
    color: #222;
}

.title {
    text-align: center;
    font-size: 3em;
    font-weight: 600;
    color:#FFD700;
    margin-bottom: 1rem;
}

.chat-container {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin: 2rem auto;
    max-width: 800px;
    width: 90%;
}

.chat-bubble {
    padding: 1rem 1.5rem;
    border-radius: 1rem;
    max-width: 75%;
    font-size: 1.05rem;
    line-height: 1.5;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}

.user {
    align-self: flex-end;
    background-color: #2563eb;
    color: white;
}

.bot {
    align-self: flex-start;
    background-color: #e5e7eb;
    color: #111827;
}

.stButton > button {
    background-color: #10b981;
    color: white;
    padding: 0.6rem 1.2rem;
    font-size: 1rem;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.3s ease;
    margin-top: 1rem;
}

.stButton > button:hover {
    background-color: #059669;
}

.stTextInput > div > input {
    font-size: 1.1rem;
    padding: 0.75rem;
    border: 1px solid #cbd5e1;
    border-radius: 0.5rem;
    width: 100%;
    margin-bottom: 0.5rem;
    background-color: #ffffff;
}
</style>
""", unsafe_allow_html=True)


# ---- Title ----
st.markdown('<div class="title">Ai-ChatBot</div>', unsafe_allow_html=True)

# ---- Chat History ----
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---- User Input ----
query = st.text_input("💬 Type your message or click Speak:", "")

# ---- Speak Button ----
col1, col2 = st.columns([1, 6])
with col1:
    if st.button("🎤 Speak"):
        with st.spinner("Listening..."):
            try:
                spoken_query = SpeechRecognition()
                st.success(f"🗣️ You said: {spoken_query}")
                query = spoken_query
            except Exception as e:
                st.error(f"❌ Speech recognition failed: {e}")

# ---- Send Button ----
with col2:
    if st.button("🚀 Send"):
        if query.strip():
            answer = ChatBot(query)
            st.session_state.chat_history.append(("You", query))
            st.session_state.chat_history.append(("Bot", answer))
            st.rerun()


# ---- Show Conversation ----
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for sender, msg in st.session_state.chat_history:
    role_class = "user" if sender == "You" else "bot"
    st.markdown(
        f'<div class="chat-bubble {role_class}"><strong>{sender}:</strong><br>{msg}</div>',
        unsafe_allow_html=True
    )
st.markdown('</div>', unsafe_allow_html=True)
