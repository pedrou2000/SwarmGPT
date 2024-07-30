import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from agent_coder_plus.data_classes.AgentCoderPlusState import AgentCoderPlusState
from agent_coder_plus.langgraphs.agent_coder_plus_coder import get_agent_coder_plus_coder_graph
from agent_coder_plus.langgraphs.agent_coder_plus_tests import get_agent_coder_plus_tests_graph

def get_agent_coder_plus_graph():
    graph = StateGraph(AgentCoderPlusState)

    graph.add_node("Test Generator", get_agent_coder_plus_tests_graph().compile())
    graph.add_node("Coder", get_agent_coder_plus_coder_graph().compile())

    graph.set_entry_point("Test Generator")
    graph.add_edge("Test Generator", "Coder")
    graph.add_edge("Coder", END)

    return graph

if __name__ == "__main__":
    graph = get_agent_coder_plus_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
