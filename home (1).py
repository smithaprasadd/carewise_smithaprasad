import streamlit as st

def home_page():
    st.markdown(
        """
        <style>
        .main {
            background-color: #DFF6DD !important;  
            color: #333333 !important;  
        }
        [data-testid="stAppViewContainer"] {
            background-color: #DFF6DD !important;
            color: #333333 !important;
        }
        h1, h2, h3, h4, h5, h6, p, label {
            color: #333333 !important;  
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("hero_image.png", use_container_width=True)

    st.header("Why Choose Our AI Health Bot?")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.image("instant_health_advice.png", use_container_width=True)
        st.subheader("Instant Health Advice")
        st.write("Get health advice instantly based on your symptoms.")
    with col2:
        st.image("247_availability.png", use_container_width=True)
        st.subheader("24/7 Availability")
        st.write("Our AI bot is available round the clock to assist you.")
    with col3:
        st.image("personalized_care.png", use_container_width=True)
        st.subheader("Personalized Care")
        st.write("Receive personalized care recommendations.")
    with col4:
        st.image("secure_data_handling.png", use_container_width=True)
        st.subheader("Secure Data Handling")
        st.write("Your data is secure with us.")

    st.header("How It Works")
    st.write("1. *Input Your Symptoms:* Enter your symptoms into the AI bot.")
    st.write("2. *Get AI-Based Guidance:* Receive AI-based health recommendations.")
    st.write("3. *Receive Treatment Recommendations:* Get suggestions based on your symptoms.")

    st.header("What People Say")
    st.write("“This AI bot is a game-changer. It gave me instant health advice when I needed it the most.”")
    st.write("“Highly recommend this service. It's fast, reliable, and always available.”")

    st.header("Get in Touch")
    contact_form = """
    <form action="https://formsubmit.co/YOUR_EMAIL" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required>
        <input type="email" name="email" placeholder="Your Email" required>
        <textarea name="message" placeholder="Your Message" required></textarea>
        <button type="submit">📩 Send</button>
    </form>
    """
    st.markdown(contact_form, unsafe_allow_html=True)
