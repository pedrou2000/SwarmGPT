import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from data_classes.MACMState import MACMState
from langgraphs.macm import get_macm_graph
from llm_agents.AgentMetaMACMController import AgentMetaMACMController
from llm_agents.AgentIndividualMathSolver import AgentIndividualMathSolver

def router(state: MACMState):
    if state.current_meta_iterations == state.n_macm_iterations:
        if not state.macm_completed:
            state.macm_completed = True
            response = "SingleAgentContinue"
        else:
            response = "MetaMACMComplete"

    else:
        if not state.macm_completed:
            response = "MACMContinue"
        else:
            response = "SingleAgentContinue"
    return response

def get_meta_macm_graph():
    graph = StateGraph(MACMState)

    graph.add_node("MACM", get_macm_graph().compile())
    graph.add_node("AgentIndividualMathSolver", AgentIndividualMathSolver())
    graph.add_node("AgentMetaMACMController", AgentMetaMACMController())

    graph.set_entry_point("MACM")
    graph.add_edge("MACM", "AgentMetaMACMController")
    graph.add_edge("AgentIndividualMathSolver", "AgentMetaMACMController")
    graph.add_conditional_edges(
        "AgentMetaMACMController",
        router,
        {
            "MetaMACMComplete": END,
            "MACMContinue": "MACM",
            "SingleAgentContinue": "AgentIndividualMathSolver"
        }
    )

    return graph

if __name__ == "__main__":
    graph = get_meta_macm_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
