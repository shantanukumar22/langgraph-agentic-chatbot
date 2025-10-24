import streamlit as st
from src.langgraphagenticai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenticai.LLMS.groqllm import GroqLLM
from src.langgraphagenticai.graph.graph_builder import GraphBuilder
from src.langgraphagenticai.ui.streamlitui.display_result import DisplayResultStreamlit 
def load_langgraph_agenticai_app():
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    if not user_input:
        st.error("failed to load the user input from the UI")
        return
    user_message=st.chat_input("Enter your message:")
    if user_message:
        try:
            ### configure the LLM
            obj_llm_config=GroqLLM(user_control_input=user_input)
            model=obj_llm_config.get_llm_model()
            if not model:
                st.error("llm model could not be initialized")
                return
            #initialize and set up the graph based on use-case
            usecase=user_input.get("selected_usecase")
            if not usecase:
                st.error("no use case selected")
                return
            ## graph builder
            graph_builder=GraphBuilder(model)
            DisplayResultStreamlit(usecase,graph,user_message).display_result_on_ui
            try:
                graph=graph_builder.setup_graph(usecase)
            except Exception as e:
                st.error(f"Error graph set up failed: {e}")
                return

        except Exception as e: 
            st.error(f"error in working of the app: {e}")
            return