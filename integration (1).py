import streamlit as st
import speech_recognition as sr
import google.generativeai as genai
from googletrans import Translator
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

# Set Streamlit page config (MUST be the first command)

# Configure API Key (Replace with your API key)
API_KEY = "AIzaSyBXMxjZyXv29Dftocn5ZLeKjIZUPZehty4"
genai.configure(api_key=API_KEY)


# System Instructions for AI
SYSTEM_INSTRUCTIONS = """
You are CareWise, an AI health assistant providing concise, responsible, and informative responses.

- Prioritize accuracy and clarity.
- Suggest over-the-counter (OTC) medications only if appropriate, including dosage details:
  - Tablets: Specify the count, timing, and whether to take them before or after food (e.g., 1 tablet twice a day after food).
  - Syrups: Provide the dosage in milliliters, timing, and food-related instructions (e.g., 10ml twice a day before food).
- Include one natural remedy as an alternative when relevant.
- Avoid disclaimers like "I'm not a doctor," but do not provide diagnoses.
- If a message is not health-related, gently steer the conversation back to health topics.
"""

# Language selection for speech recognition and AI responses


# Function to check if a message is a greeting
def is_greeting(message):
    greetings = ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]
    return message.lower() in greetings

# Function to determine if a message is health-related
def is_health_related(message):
    """Uses AI to determine if the input is health-related."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
    {SYSTEM_INSTRUCTIONS}
    Determine if the following message is about health, symptoms, or medical advice.
    Answer only 'yes' or 'no'.
    
    Message: {message}
    """
    response = model.generate_content(prompt)
    return "yes" in response.text.lower()
language_map = {
    "English": "en",
    "Telugu (తెలుగు)": "te",
    "Hindi (हिन्दी)": "hi"
}

selected_language = st.selectbox("🌍 Select your language:", list(language_map.keys()))

# Function to generate medical responses and translate them
def get_medical_response(message):
    """Generates a response with specific OTC medications if relevant and translates it to the selected language."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""
    {SYSTEM_INSTRUCTIONS}
    Provide a short response (2-3 sentences max) for the given health concern.
    
    Message: {message}
    """
    response = model.generate_content(prompt)
    response_text = response.text.strip()

    # Translate response if a non-English language is selected
    if selected_language != "English":
        response_text = translate_text(response_text, language_map[selected_language])

    return response_text

# Function to translate text into the selected language
def translate_text(text, target_lang):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_lang).text
        return translated_text
    except Exception as e:
        return text  # Fallback to original text if translation fails


# Function for voice input with multilingual support
# Function for voice input with multilingual support
def get_voice_input(selected_language):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info(f"🎤 Speak now... (Listening in {selected_language})")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio, language=language_map[selected_language])
            st.success(f"🗣 You said: {text}")
            return text
        except sr.UnknownValueError:
            st.error("Sorry, I couldn't understand. Please try again.")
        except sr.RequestError:
            st.error("Network error. Check your internet connection.")
    return ""


def run():
    global selected_language
    st.markdown(
    """
            <style>
            /* Background Color */
            .stApp {
                background-color:rgb(120, 219, 118); /* Light Beige */
            }
            
            /* Header Styling */
            h1 {
                text-align: center;
                color: #0077B6; /* Deep Blue */
                font-size: 36px;
                font-weight: bold;
            }
            
            h2 {
                text-align: center;
                color: #198754; /* Bright Green */
                font-size: 22px;
            }

            
            /* Chat Container */
            .chat-container {
                max-width: 600px;
                margin: auto;
            }

            /* Assistant Chat Bubble */
            .assistant-message {
                background-color: #E3F2FD; /* Light Blue */
                color: #0A66C2; /* Dark Blue */
                padding: 12px;
                border-radius: 15px;
                width: fit-content;
                max-width: 70%;
                margin: 10px 0;
                text-align: left;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            }

            /* User Chat Bubble */
            .user-message {
                background-color: #D4EDDA; /* Light Green */
                color: #155724; /* Dark Green */
                padding: 12px;
                border-radius: 15px;
                width: fit-content;
                max-width: 70%;
                margin: 10px 0 10px auto;
                text-align: right;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            }

            /* Footer */
            .footer {
                text-align: center;
                font-size: 14px;
                color: white;
                background-color: #198754;
                padding: 10px;
                border-radius: 8px;
            }
            /* Specific Styling for Language Selectbox */
.language-selectbox-container {
    display: flex;
    justify-content: center;
    margin-top: 20px;
}

.language-selectbox {
    font-size: 18px;
    font-weight: bold;
    color:rgb(18, 24, 27);
    border: 2px solid #0077B6 !important;
    border-radius: 8px;
    padding: 8px;
    background-color: white !important;
}

    """,
    unsafe_allow_html=True
)

    st.markdown("<h1>💬 CareWise: AI Health Chat</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Let’s talk about your health. I’m here to assist you.</h3>", unsafe_allow_html=True)
    st.markdown('<div class="language-selectbox-container">', unsafe_allow_html=True)
    selected_language = st.selectbox("🌍 Select your language:", list(language_map.keys()))

    # Initialize Chat History
    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "Hello! How are you feeling today?"}  # No extra 🤖 here
        ]

    # Display Chat History
    st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
    for msg in st.session_state.messages:
        role_class = "assistant-message" if msg["role"] == "assistant" else "user-message"
        icon = "🤖" if msg["role"] == "assistant" else "👤"  # Automatically add the correct icon
        st.markdown(
            f"<div class='{role_class}'><span class='icon'>{icon}</span>{msg['content']}</div>", 
            unsafe_allow_html=True
        )
    st.markdown("</div>", unsafe_allow_html=True)

    # Text Input
    user_input = st.chat_input("Type your message...")

    # Voice Input Button
    if st.button("🎤 Voice Input"):
        voice_text = get_voice_input(selected_language)
        if voice_text:
            user_input = voice_text  # Use voice input as text input


    if user_input:
    # Add User Message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.markdown(f"<div class='user-message'><span class='icon'>👤</span>{user_input}</div>", unsafe_allow_html=True)

        if is_greeting(user_input):
            response = "Hello! How can I assist you with your health today?"
        elif is_health_related(user_input):
            response = get_medical_response(user_input)
        else:
            response = "I'm here to discuss your health. Can you describe any symptoms or concerns?"

    # Ensure the response is translated before displaying
        if selected_language != "English":
            response = translate_text(response, language_map[selected_language])

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.markdown(f"<div class='assistant-message'><span class='icon'>🤖</span>{response}</div>", unsafe_allow_html=True)

    # Footer
    st.markdown("<div class='footer'>⚠ CareWise provides AI-generated medical insights. Always consult a doctor for serious conditions.</div>", unsafe_allow_html=True)
    st.markdown("<div class='footer'>Made with ❤ for better health assistance.</div>", unsafe_allow_html=True)
    
    

