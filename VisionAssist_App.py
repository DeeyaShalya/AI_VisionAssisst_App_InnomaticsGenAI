import streamlit as st
from PIL import Image
import pyttsx3
import os
import pytesseract  
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAI
import threading

# Set Tesseract OCR path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Initialize Google Generative AI with API Key
GEMINI_API_KEY = "AIzaSyBbDQ2Tu3W9Ilj-GBF6uYoqSkQKyUVqQsA"
os.environ["GOOGLE_API_KEY"] = GEMINI_API_KEY

llm = GoogleGenerativeAI(model="gemini-1.5-pro", api_key=GEMINI_API_KEY)

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

# Function to handle Text-to-Speech in a separate thread
def text_to_speech(text):
    def speak():
        engine.say(text)
        engine.runAndWait()

    # Run the speak function in a new thread to avoid blocking
    threading.Thread(target=speak).start()

# Streamlit Page Configuration
st.set_page_config(page_title="VisionAssist", layout="wide", page_icon="👁️")

# Page Styles
st.markdown(""" 
    <style> 
    .main-title { 
        font-size: 48px; 
        font-weight: bold; 
        text-align: center; 
        color: #0662f6; 
    } 
    .subtitle { 
        font-size: 18px; 
        color: #555; 
        text-align: center; 
    } 
    .feature-header { 
        font-size: 22px; 
        color: #333; 
        font-weight: bold; 
        margin-top: 20px; 
    } 
    .chat-container { 
        background-color: #f7f7f7; 
        padding: 20px; 
        border-radius: 8px; 
        margin-top: 20px; 
    } 
    </style> 
""", unsafe_allow_html=True)

# Page Title and Description
st.markdown('<div class="main-title">VisionAssist 👁️</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI for Scene Understanding & Speech for the Visually Impaired 🗣️</div>', unsafe_allow_html=True)

# Sidebar for About Section
st.sidebar.title("ℹ️ About")
st.sidebar.markdown(""" 
    📌 **Features** 
    - 🔍 **Describe Scene**: Get AI insights about the image. 
    - 🤖 **Chatbot**: Interact with an AI-powered chatbot that responds to your queries. 
    - 🔊 **Read Aloud**: Listen to scene descriptions and chatbot responses. 

    💡 **How it helps**: 
    Assists visually impaired users by providing scene descriptions, speech synthesis, and chatbot interactions. 

    🤖 **Powered by**: 
    - **Google Gemini API** for scene understanding. 
    - **pyttsx3** for text-to-speech. 
    """, unsafe_allow_html=True)

# Image Upload Section
st.markdown("<h3 class='feature-header'>📤 Upload an Image</h3>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("Drag and drop or browse an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Function to describe scene
def generate_scene_description(input_prompt, image_data):
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content([input_prompt, image_data[0]])
    return response.text

# Chatbot setup
llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])

# Initialize the session state for the chatbot
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "ai", "text": "Hi there! I am a helpful AI Assistant. How can I help you today?"}]

# Chatbot UI
st.markdown("<h3 class='feature-header'>💬 Chat with AI</h3>", unsafe_allow_html=True)
for message in st.session_state.messages:
    if message["role"] == "ai":
        st.chat_message("ai").write(message["text"])
    else:
        st.chat_message("human").write(message["text"])

# User input for chatbot
human_prompt = st.chat_input("Say something...")

if human_prompt:
    st.session_state.messages.append({"role": "human", "text": human_prompt})
    st.chat_message("human").write(human_prompt)

    response = chatbot.send_message(human_prompt)
    st.session_state.messages.append({"role": "ai", "text": response.text})
    st.chat_message("ai").write(response.text)

    # Read aloud the chatbot response in a separate thread
    text_to_speech(response.text)

# Buttons for Scene Description and Read Aloud
st.markdown("<h3 class='feature-header'>⚙️ Features</h3>", unsafe_allow_html=True)
col1, col2 = st.columns(2)

scene_button = col1.button("🔍 Describe Scene")
read_aloud_button = col2.button("🔊 Read Aloud Description")

# Input prompt for Scene Understanding
input_prompt = """
You are an AI assistant helping visually impaired individuals by describing the scene in the image. Provide:
1. List of items detected in the image with their purpose.
2. Overall description of the image.
3. Suggestions for actions or precautions for the visually impaired.
"""

# Process Scene Description
if uploaded_file:
    image_data = [{"mime_type": uploaded_file.type, "data": uploaded_file.getvalue()}]

    if scene_button:
        with st.spinner("Generating scene description..."):
            response = generate_scene_description(input_prompt, image_data)
            st.markdown("<h3 class='feature-header'>🔍 Scene Description</h3>", unsafe_allow_html=True)
            st.write(response)

            # Read aloud scene description in a separate thread
            text_to_speech(response)

# Footer
st.markdown("""
    <hr>
    <footer style="text-align:center;">
        <p>Powered by <strong>Google Gemini API</strong> | Built with ❤️ using Streamlit</p>
    </footer>
""", unsafe_allow_html=True)

# Additional Sidebar Footer
st.sidebar.markdown("""
    <hr>
    <footer style="text-align:center;">
        <p>Powered by <strong>Google Gemini API</strong> | Built with ❤️ using Streamlit</p>
    </footer>
""", unsafe_allow_html=True)
