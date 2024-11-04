import streamlit as st
import time


st.title("Counter THING")

if "is_running" not in st.session_state:
    st.session_state.is_running = False

# Create a session state that will keep track of the counter and the running state
if 'counter' not in st.session_state:
    st.session_state.counter = 0
    st.session_state.is_running = False

def start_counter():
    st.session_state.is_running = True

# Button that starts the counter
if st.button("Start"):
    start_counter()
    
if st.button("Stop"):
    st.session_state.is_running = False
    
if st.button("Reset"):
    st.session_state.counter = 0
    st.session_state.is_running = False

# This displays the current count
st.subheader(f"{st.session_state.counter}")

# If the counter is running, it will increment the counter every second
if st.session_state.is_running:
    while True:
        time.sleep(1)  # Wait for 1 second
        st.session_state.counter += 1
        st.rerun()  # Reruns the app to update the display
