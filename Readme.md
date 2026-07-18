# AI Chatbot (Groq API)

A simple, interactive AI chatbot built with Streamlit and powered by the Groq API (Llama 3.1 model). Features a clean chat interface with persistent conversation history.

## Features

- Real-time AI responses using Llama 3.1 model via Groq API
- Clean, chat-style interface (like WhatsApp/ChatGPT)
- Conversation history maintained during the session
- Simple sidebar with app info
- Fast responses powered by Groq's inference engine

## How It Works

1. User types a message in the chat input box
2. The message is sent to the Groq API along with the conversation context
3. The AI (Llama 3.1) generates a response
4. Both user message and AI response are displayed in a chat-style interface and saved in session history

## Technologies Used

- Python
- Streamlit (for the web interface)
- Groq API (for AI responses)
- `openai` library (used to interact with Groq's OpenAI-compatible API)
- `python-dotenv` (for secure API key management)

## How to Run

1. Install the required libraries:
```bash
pip install streamlit openai python-dotenv
```

2. Create a `.env` file in the project folder and add your Groq API key:

3. Run the app:
```bash
streamlit run app.py
```

4. The app will open in your browser — start chatting!

## What I Learned

- Building interactive web apps with Streamlit
- Integrating third-party AI APIs (Groq) into a Python application
- Managing conversation state using Streamlit's session state
- Securely handling API keys with environment variables
- Debugging API integration issues (model availability, quota limits, provider configuration)

## Author

Abhay Singh