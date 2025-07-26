import streamlit as st
import time
from datetime import datetime
import pytz


st.markdown("""
<style>
html, body {
    overflow: hidden !important;
    height: 100% !important;
    margin: 0 !important;
    padding: 0 !important;
}
.time-container {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh !important;
    width: 100vw !important;
    position: fixed !important;
    top: 0 !important;
    left: 0 !important;
}
.big-time {
    font-size: 20vw !important;
    font-family: monospace;
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

clock_container = st.empty()
hk_tz = pytz.timezone('Asia/Hong_Kong')

now = datetime.now(hk_tz)
current_time = now.strftime("%H:%M:%S")
current_date = now.strftime("%A, %B %d, %Y")

while True:
    now = datetime.now(hk_tz)
    current_time = now.strftime("%H:%M:%S")
    
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
    
    time.sleep(0.9)
