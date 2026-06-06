import streamlit as st
from groq import Groq

# Page Configuration
st.set_page_config(page_title="Nexa AI", page_icon="⚡", layout="centered")

# Dark Mode Styling
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    </style>
""", unsafe_allow_html=True)

st.title("⚡ Nexa AI")
st.subheader("Your Personal Assistant")

# Direct API Key setup
api_key = "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"

if not api_key:
    st.error("Error: API Key is missing.")
    st.stop()

client = Groq(api_key=api_key)

# Initialize Session State
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are Nexa, a helpful and witty AI assistant."}
    ]

# Display Chat History
for message in st.session_state.messages:
    if message["role"] != "system":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# User Input Handling
if prompt := st.chat_input("Ask Nexa anything..."):
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
