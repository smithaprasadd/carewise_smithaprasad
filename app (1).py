import streamlit as st
from pages import chatbot, home, services

# Set page configuration
st.set_page_config(page_title="CareWise - AI Health Assistant", layout="wide", page_icon="💬")

# Hide Sidebar & Default Header
st.markdown(
    """
    <style>
        [data-testid="stSidebarNav"], header { display: none !important; }
        .nav {
            background-color: #B8E6B3; 
            padding: 12px;
            border-radius: 10px;
            text-align: center;
        }
        .nav a {
            color: #3D9970; 
            text-decoration: none;
            margin: 20px;
            font-weight: bold;
            font-size: 20px;
            padding: 10px;
            border-radius: 10px;
            transition: background 0.3s;
        }
        .nav a:hover {
            background-color: #A0D6A0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Initialize session state for navigation
query_params = st.query_params
page = query_params.get("page", "home")

# Navigation Bar
st.markdown(
    f"""
    <div class="nav">
        <a href="?page=home">🏠 Home</a>
        <a href="?page=services">💼 Services</a>
        <a href="?page=chat">💬 AI Chat</a>
    </div>
    """,
    unsafe_allow_html=True,
)

# Load pages dynamically
if page == "home":
    home.home_page()
elif page == "services":
    services.services_page()
elif page == "chat":
    chatbot.run()
