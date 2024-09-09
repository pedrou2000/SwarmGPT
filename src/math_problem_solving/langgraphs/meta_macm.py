import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from data_classes.MACMState import MACMState
from langgraphs.macm import get_macm_graph
from langgraphs.macm_tests import get_macm_tests_graph
from llm_agents.AgentMetaMACMController import AgentMetaMACMController
from llm_agents.AgentIndividualMathSolver import AgentIndividualMathSolver
from llm_agents.AgentSolutionEvaluator import AgentSolutionEvaluator

def router(state: MACMState):
    if state.current_meta_iterations == state.n_multi_agent_iterations:
        if not state.multi_agent_completed:
            state.multi_agent_completed = True
            response = "SingleAgentContinue"
        else:
            response = "MetaMACMComplete"

    else:
        if not state.multi_agent_completed:
            response = "MACMContinue"
        else:
            response = "SingleAgentContinue"
    return response

def get_meta_macm_graph():
    graph = StateGraph(MACMState)

    graph.add_node("Test Designer", get_macm_tests_graph().compile())
    graph.add_node("MACM", get_macm_graph().compile())
    graph.add_node("Chain of Thought Agent", AgentIndividualMathSolver())
    graph.add_node("Meta Controller", AgentMetaMACMController())
    graph.add_node("Solution Evaluator", AgentSolutionEvaluator())

    graph.set_entry_point("Test Designer")
    graph.add_edge("Test Designer", "Meta Controller")
    graph.add_conditional_edges(
        "Meta Controller",
        router,
        {
            "MetaMACMComplete": "Solution Evaluator",
            "MACMContinue": "MACM",
            "SingleAgentContinue": "Chain of Thought Agent"
        }
    )

    graph.add_edge("MACM", "Meta Controller")
    graph.add_edge("Chain of Thought Agent", "Meta Controller")

    graph.add_edge("Solution Evaluator", END)

    return graph

if __name__ == "__main__":
    graph = get_meta_macm_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
