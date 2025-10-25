from langgraph.graph import StateGraph,START,END
from src.langgraphagenticai.state.state import State
from langgraph.prebuilt import tools_condition,tool_node
from src.langgraphagenticai.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphagenticai.tools.search_tool import get_tools,create_tools_node
from src.langgraphagenticai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
class GraphBuilder():
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
    def basic_chatbot_build_graph(self):
        self.basic_chatbot_node=BasicChatbotNode(self.llm)
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition) #if there will be toolcall it will go to the tool otherwise go to  the end 
        self.graph_builder.add_node("tools","chatbot")
    def chatbot_with_tools_build_graph(self):
         """
        Builds an advanced chatbot graph with tool integration.
        This method creates a chatbot graph that includes both a chatbot node 
        and a tool node. It defines tools, initializes the chatbot with tool 
        capabilities, and sets up conditional and direct edges between nodes. 
        The chatbot node is set as the entry point.
        """
         ## defining the tool and the tool node
         tools=get_tools()
         tool_node=create_tools_node(tools)
         ## define the LLm
         llm=self.llm
         ## define the chatbot node
         obj_chatbot_with_node=ChatbotWithToolNode(llm)
         chatbot_node=obj_chatbot_with_node.create_chatbot(tools)
         self.graph_builder.add_node("chatbot",chatbot_node)
         self.graph_builder.add_node("tools",tool_node)
         ##defining the conditional and direct edges
         self.graph_builder.add_edge(START,"chatbot")
         self.graph_builder.add_conditional_edges("chatbot",tools_condition)
         self.graph_builder.add_edge("tools","chatbot")
    def setup_graph(self,usecase:str):
        """set's up the graph for the selected use-case"""
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
        if usecase == "Chatbot With Web":
            self.chatbot_with_tools_build_graph()
        return self.graph_builder.compile()
