import streamlit as st
import pytz

# Initialize session state variables
if "inside_clock" not in st.session_state:
    st.session_state.inside_clock = False

if "timezone" not in st.session_state:
    st.session_state.timezone = None

def Clock():
    st.title("Live Clock")

    # Validate timezone
    if not st.session_state.timezone:
        st.error("No timezone selected. Please go back and select a timezone.")
        if st.button("Back to Timezone Selection"):
            st.session_state.inside_clock = False
            st.rerun()
        return

    try:
        timezone = pytz.timezone(st.session_state.timezone)
    except pytz.exceptions.PytzError:
        st.error("Invalid timezone selected. Please go back and select a valid timezone.")
        if st.button("Back to Timezone Selection"):
            st.session_state.inside_clock = False
            st.rerun()
        return

    # Create an empty placeholder for the clock
    clock_placeholder = st.empty()

    # JavaScript code for the real-time clock with time and timezone on separate lines
    js_code = f"""
    <div style="font-family: 'Orbitron', sans-serif; color: #66ff99; text-align: center; padding: 20px;">
        <div id="time" style="font-size: 48px;"></div>
        <div id="timezone" style="font-size: 24px; margin-top: 10px;"></div>
    </div>
    <script>
        function updateClock() {{
            const now = new Date();
            const options = {{
                timeZone: '{st.session_state.timezone}',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit',
                hour12: true
            }};
            const timeString = now.toLocaleTimeString('en-US', options);
            document.getElementById('time').innerText = timeString;
            document.getElementById('timezone').innerText = '{st.session_state.timezone}';
        }}
        updateClock(); // Initial call
        setInterval(updateClock, 1000); // Update every second
    </script>
    <link href="https://fonts.googleapis.com/css?family=Orbitron" rel="stylesheet">
    """

    # Embed the JavaScript clock in the placeholder
    clock_placeholder.html(js_code, height=200)

    # Back button to return to timezone selection
    if st.button("Back to Timezone Selection"):
        st.session_state.inside_clock = False
        st.rerun()

# Check boolean directly instead of using `in`
if not st.session_state.inside_clock:
    selected_timezone = st.selectbox("Select your timezone", [None] + list(pytz.all_timezones))
    st.write(f"Selected: {selected_timezone}")

    if st.button(f"Go to {selected_timezone}'s Live Clock" if selected_timezone else "Please select your timezone first", disabled=not selected_timezone):
        if selected_timezone:
            st.session_state.timezone = selected_timezone
            st.session_state.inside_clock = True
            st.rerun()
else:
    Clock()
