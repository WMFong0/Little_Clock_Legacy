import streamlit as st
import time
from datetime import datetime
import pytz

# Custom CSS with percentage-based sizing
st.markdown("""
<style>
.time-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 90vh;
}
.big-time {
    font-size: 20vw !important;
    line-height: 1;
    white-space: nowrap;
    margin: 0;
    padding: 0;
}
.date-header {
    font-size: 3vw !important;
    margin-bottom: 2vh;
    color: #666;
}
.timezone-label {
    font-size: 2vw !important;
    color: #888;
    margin-top: 1vh;
}
</style>
""", unsafe_allow_html=True)

# Remove Streamlit UI elements
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stApp {padding: 0;}
</style>
""", unsafe_allow_html=True)

# Create a single container
clock_container = st.empty()

# Hong Kong timezone
hk_tz = pytz.timezone('Asia/Hong_Kong')

while True:
    # Get current time in Hong Kong
    now = datetime.now(hk_tz)
    
    # Format time and date
    current_time = now.strftime("%H:%M:%S")
    current_date = now.strftime("%A, %B %d, %Y")
    
    # Update the display
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
