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

    graph.add_node("Test Designer", get_agent_coder_plus_tests_graph().compile())
    graph.add_node("Meta Programmer", get_agent_coder_plus_coder_graph().compile())

    graph.set_entry_point("Test Designer")
    graph.add_edge("Test Designer", "Meta Programmer")
    graph.add_edge("Meta Programmer", END)

    return graph

if __name__ == "__main__":
    graph = get_agent_coder_plus_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
