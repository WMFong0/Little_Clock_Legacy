import streamlit as st
import time
from datetime import datetime
# Custom CSS with percentage-based sizing
st.markdown("""
<style>
.big-font {
    font-size: 12vw !important;  /* Viewport width percentage */
    text-align: center;
    margin-top: 10vh;
    line-height: 0.9;
}
.date-font {
    font-size: 2vw !important;  /* Viewport width percentage */
    text-align: center;
    margin-top: 1vh;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# Create placeholders
date_display = st.empty()
time_display = st.empty()

# Remove Streamlit UI elements
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stApp {padding-top: 0;}
</style>
""", unsafe_allow_html=True)

# Continuous clock update
while True:
    now = datetime.now()
    
    # Update date
    current_date = now.strftime("%A, %B %d, %Y")
    date_display.markdown(
        f'<p class="date-font">{current_date}</p>',
        unsafe_allow_html=True
    )
    
    # Update time
    current_time = now.strftime("%H:%M:%S")
    time_display.markdown(
        f'<p class="big-font">{current_time}</p>',
        unsafe_allow_html=True
    )
    
    time.sleep(1)
