import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI

def load_langgraph_agenticai_app():
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("failed to load the user input from the UI")
        return
    user_message=st.chat_input("Enter your message:")
