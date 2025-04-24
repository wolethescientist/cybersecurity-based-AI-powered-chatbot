import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-2.0-flash')

# Set page configuration
st.set_page_config(
    page_title="Cybersecurity FAQ Chatbot",
    page_icon="🔒",
    layout="wide"
)

# Add custom CSS
st.markdown("""
    <style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
        background-color: #1a1a1a;
        color: #ffffff;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .bot {
        background-color: #2d2d2d;
        color: #ffffff;
    }
    .user {
        background-color: #404040;
        color: #ffffff;
    }
    /* Additional styling for better visibility */
    .stTextInput input {
        background-color: #333333;
        color: #ffffff;
        border-color: #4d4d4d;
    }
    .stButton button {
        background-color: #4d4d4d;
        color: #ffffff;
    }
    .stMarkdown {
        color: #ffffff;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

def get_cybersecurity_response(user_input):
    # Prepare context and prompt
    context = """You are a cybersecurity expert chatbot. Provide accurate, helpful, and concise answers to questions about cybersecurity.
    Focus on best practices, common threats, security measures, and practical advice. If you're unsure about something, say so.
    Keep responses clear and accessible for users with varying technical backgrounds."""
    
    prompt = f"{context}\n\nUser Question: {user_input}\n\nResponse:"
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"I apologize, but I encountered an error: {str(e)}"

# Main UI
st.title("🔒 Cybersecurity FAQ Chatbot")
st.markdown("""
Welcome to the Cybersecurity FAQ Chatbot! Ask any questions about:
- Cybersecurity best practices
- Common security threats
- Password management
- Network security
- Data protection
- And more!
""")

# User input
user_question = st.text_input("Ask your cybersecurity question:", key="user_input")

# Handle user input
if st.button("Send"):
    if user_question:
        # Get bot response
        bot_response = get_cybersecurity_response(user_question)
        
        # Add to chat history
        st.session_state.chat_history.append(("user", user_question))
        st.session_state.chat_history.append(("bot", bot_response))
    else:
        st.warning("Please enter a question!")

# Display chat history
for role, message in st.session_state.chat_history:
    if role == "user":
        st.markdown(f'<div class="chat-message user">👤 **You**: {message}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-message bot">🤖 **Bot**: {message}</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("*Powered by Gemini AI - Your Cybersecurity Assistant*") 