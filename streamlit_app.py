import streamlit as st
import time
from IPython.display import clear_output
from datetime import datetime
import pytz

hong_kong_timezone = pytz.timezone('Asia/Hong_Kong')

while True:
    now_utc = datetime.now(pytz.utc)
    now_hong_kong = now_utc.astimezone(hong_kong_timezone)
    st.title(f"{now_hong_kong.strftime("%Y/%m/%d %I:%M:%S%p %A")}")
    time.sleep(1)