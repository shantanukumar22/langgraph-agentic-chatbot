from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
class GraphBuilder():
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_edge("chatbot",END)
    def chatbot_with_tools_build_graph(self):
         """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
         ## defining the tool and the tool node
         

    def setup_graph(self,usecase:str):
        """set's up the graph for the selected use-case"""
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        return self.graph_builder.compile()
