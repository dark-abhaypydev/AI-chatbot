# AI Chatbot with Groq API integration
import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

# Page ka title aur icon set kiya
st.set_page_config(page_title="My AI Chatbot", page_icon="🤖", layout="centered")

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

client = OpenAI(
    api_key=groq_api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Sidebar mein info dia hai
with st.sidebar:
    st.header("About")
    st.write("Ye ek AI chatbot hai jo Groq API aur Llama model use karke sawalon ka jawab deta hai.")
    st.write("Built by Abhay Singh")

st.title("🤖 My AI Chatbot")
st.write("Mujhse kuch bhi poocho!")

# Chat history yaad rakhne ke liye (taaki purane messages screen pe dikhte rahein)
if "messages" not in st.session_state: 
    st.session_state.messages = []

# Purane saare messages ko screen pe dikhaya
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User se naya message liya
user_input = st.chat_input("Apna sawal likho...")

if user_input:
    # User ka message history mein save kiya aur screen pe dikhaya
    st.session_state.messages.append({"role": "user", "content": user_input}) # ye line ye krti hai ki user ka message history mein save ho jaye
    with st.chat_message("user"):
        st.write(user_input)

    # AI se jawab mangwaya, loading spinner ke saath
    with st.spinner("Soch raha hoon..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        ai_reply = response.choices[0].message.content

    # AI ka jawab history mein save kiya aur screen pe dikhaya
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    with st.chat_message("assistant"):
        st.write(ai_reply)