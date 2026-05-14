import streamlit as st
import time

st.set_page_config(
    page_title="AI CV Analysis",
    page_icon="🤖",
    layout="centered"
)
with st.spinner("Loading..."):
    time.sleep(2)
    st.snow()
    st.title("An Ai-powered CV Analysis")

