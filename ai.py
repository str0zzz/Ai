import streamlit as st
from groq import Groq
import os

# --- Page Setup ---
st.set_page_config(page_title="Nexa AI", page_icon="⚡", layout="centered")

# --- UI Customization ---
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Nexa AI")
st.subheader("Your Personal Assistant")

# --- Logic ---
api_key = os.environ.get("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")

if not api_key:
    st.error("Please set your GROQ_API_KEY in Render Environment Variables.")
    st.stop()

client = Groq(api_key=api_key)

# Session History
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Nexa, a helpful and witty AI assistant. Keep answers concise and smart."}
    ]

# Display Messages
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Enthuaariyanam?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=st.session_state.messages,
            stream=True,
        )
        response = st.write_stream(stream)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
