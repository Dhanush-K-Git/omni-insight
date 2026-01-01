import streamlit as st
import os
from dotenv import load_dotenv
from google import genai

# 1. SETUP: Standard Page Config
st.set_page_config(page_title="Omni-Insight AI", layout="centered")
load_dotenv()

# 2. MEMORY BANK: This is the critical fix
# We store the 'client' and 'chat' in session_state so they NEVER close early
if "client" not in st.session_state:
    st.session_state.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

if "chat" not in st.session_state:
    st.session_state.chat = st.session_state.client.chats.create(model="gemini-flash-latest")

if "messages" not in st.session_state:
    st.session_state.messages = []

# UI Header
st.title("🛡️ Omni-Insight: PDF Intelligence")
st.write("Upload a document and chat with its data in real-time.")

# 3. SIDEBAR: File Upload
with st.sidebar:
    st.header("Document Center")
    uploaded_file_raw = st.file_uploader("Upload PDF", type="pdf")

# 4. CHAT DISPLAY: Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 5. LOGIC: Handle User Input
if prompt := st.chat_input("Ask about your PDF..."):
    if not uploaded_file_raw:
        st.warning("Please upload a PDF first!")
    else:
        # Add user message to history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.spinner("Analyzing..."):
            # Create a temporary file to send to Google
            with open("temp_data.pdf", "wb") as f:
                f.write(uploaded_file_raw.getbuffer())
            
            # Upload and get response
            gemini_file = st.session_state.client.files.upload(file="temp_data.pdf")
            response = st.session_state.chat.send_message(message=[gemini_file, prompt])
            
            # Save AI response to history
            st.session_state.messages.append({"role": "assistant", "content": response.text})
            with st.chat_message("assistant"):
                st.markdown(response.text)