import streamlit as st
import time
from datetime import datetime
import pytz

# Initialize session state for theme if it doesn't exist
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Custom CSS styling with theme switching
st.markdown(f"""
<style>
html, body {{
    overflow: hidden !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
    background-color: {'#121212' if st.session_state.dark_mode else '#ffffff'};
    color: {'white' if st.session_state.dark_mode else 'black'};
}}
.time-container {{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh !important;
    width: 100vw !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
}}
.big-time {{
    font-size: 20vw !important;
    font-family: monospace;
    line-height: 1;
    white-space: nowrap;
    margin: 0;
    padding: 0;
    color: {'white' if st.session_state.dark_mode else 'black'};
}}
.date-header {{
    font-size: 3vw !important;
    margin-bottom: 2vh;
    color: {'#ccc' if st.session_state.dark_mode else '#666'};
}}
.timezone-label {{
    font-size: 2vw !important;
    margin-top: 1vh;
    color: {'#aaa' if st.session_state.dark_mode else '#888'};
}}
.theme-toggle {{
    position: fixed !important;
    top: 10px !important;
    right: 10px !important;
    z-index: 1000 !important;
    background: {'#333' if st.session_state.dark_mode else '#eee'};
    border-radius: 50% !important;
    width: 40px !important;
    height: 40px !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    cursor: pointer !important;
    border: none !important;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2) !important;
}}
</style>
""", unsafe_allow_html=True)

# Remove all Streamlit UI elements
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stApp {padding: 0 !important; margin: 0 !important;}
</style>
""", unsafe_allow_html=True)

# Theme toggle button
if st.button("🌓", key="theme_toggle", help="Toggle dark mode"):
    st.session_state.dark_mode = not st.session_state.dark_mode
    st.experimental_rerun()

# Clock elements
clock_container = st.empty()
hk_tz = pytz.timezone('Asia/Hong_Kong')

# Initialize with current date and time
now = datetime.now(hk_tz)
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%A, %B %d, %Y")

while True:
    now = datetime.now(hk_tz)
    current_time = now.strftime("%H:%M:%S")
    
    # Update date only at exactly 00:00:00
    if current_time == "00:00:00":
        current_date = now.strftime("%A, %B %d, %Y")
        time.sleep(1)
    
    clock_container.markdown(
        f"""
        <div class="time-container">
            <div class="date-header">{current_date}</div>
            <div class="big-time">{current_time}</div>
            <div class="timezone-label">Hong Kong Time (HKT)</div>
        </div>
        """,
        unsafe_allow_html=True
    )
    
    time.sleep(1)
