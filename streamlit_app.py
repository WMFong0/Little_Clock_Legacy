import streamlit as st
import time
from datetime import datetime


# Create placeholders
time_placeholder = st.empty()
date_placeholder = st.empty()

while True:
    now = datetime.now()
    
    # Update time display
    current_time = now.strftime("%H:%M:%S")
    time_placeholder.header(f"Time: {current_time}")
    
    # Update date display
    current_date = now.strftime("%A, %B %d, %Y")
    date_placeholder.subheader(f"Date: {current_date}")
    
    time.sleep(1)
