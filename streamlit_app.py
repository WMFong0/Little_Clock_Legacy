import streamlit as st
import time
from datetime import datetime

# Custom CSS for full-screen clock
st.markdown("""
<style>
.time-font {
    font-size: 10rem !important;
    text-align: center;
    margin-top: 5vh;
    line-height: 1;
}
.date-font {
    font-size: 1.5rem !important;
    text-align: center;
    margin-top: 2vh;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# Create placeholders
date_display = st.empty()
time_display = st.empty()

# Remove Streamlit menu and footer
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# Continuous clock update
while True:
    now = datetime.now()
    
    # Update date (small header)
    current_date = now.strftime("%A, %B %d, %Y")
    date_display.markdown(
        f'<p class="date-font">{current_date}</p>',
        unsafe_allow_html=True
    )
    
    # Update time (main display)
    current_time = now.strftime("%H:%M:%S")
    time_display.markdown(
        f'<p class="time-font">{current_time}</p>',
        unsafe_allow_html=True
    )
    
    time.sleep(1)