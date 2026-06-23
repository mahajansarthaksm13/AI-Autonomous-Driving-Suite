import streamlit as st
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
from theme import inject_css, render_sidebar

st.set_page_config(
    page_title="Overview · AI Driving Suite",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
render_sidebar()

# Redirect to dashboard (the canonical home page)
st.switch_page("dashboard.py")
