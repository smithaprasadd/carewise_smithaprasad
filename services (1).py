import streamlit as st

def services_page():
    st.markdown("<h1 style='text-align: center; color: #0A66C2;'>💼 Our Services</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <div style='text-align: center; font-size: 18px;'>
        <p>🌟 <b>Instant Health Advice:</b> Get accurate advice tailored to your symptoms instantly.</p>
        <p>🌟 <b>24/7 Availability:</b> Always ready to assist you, no matter when or where.</p>
        <p>🌟 <b>Personalized Recommendations:</b> Enjoy health tips and care designed specifically for you.</p>
        <p>🌟 <b>Secure Data Handling:</b> We prioritize your privacy and keep your data safe.</p>
        </div>
        """,
        unsafe_allow_html=True
    )
