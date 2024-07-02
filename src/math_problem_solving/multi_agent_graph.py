import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from data_classes.MACMState import MACMState
from llm_agents.AgentConditionAnalyzer import AgentConditionAnalyzer


def get_multi_agent_summarizer_graph():
    graph = StateGraph(MACMState)

    graph.add_node("Condition Analizer", AgentConditionAnalyzer())

    graph.set_entry_point("Condition Analizer")
    graph.add_edge("Condition Analizer", END)

    return graph

if __name__ == "__main__":
    graph = get_multi_agent_summarizer_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
