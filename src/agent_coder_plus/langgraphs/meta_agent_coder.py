import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from agent_coder_plus.data_classes.MetaAgentCoderState import MetaAgentCoderState
from agent_coder_plus.langgraphs.agent_coder_plus_coder import get_agent_coder_plus_coder_graph
from agent_coder_plus.langgraphs.agent_coder_plus_tests import get_agent_coder_plus_tests_graph
from agent_coder_plus.llm_agents.AgentCoder import AgentCoder
from agent_coder_plus.llm_agents.AgentMetaController import AgentMetaController
from agent_coder_plus.llm_agents.AgentSolutionEvaluator import AgentSolutionEvaluator


def router(state):
    if state.current_meta_iterations == state.n_multi_agent_iterations:
        if not state.multi_agent_completed:
            state.multi_agent_completed = True
            response = "SingleAgentContinue"
        else:
            response = "MetaComplete"

    else:
        if not state.multi_agent_completed:
            response = "MultiAgentContinue"
        else:
            response = "SingleAgentContinue"
    return response

def get_meta_agent_coder_graph():
    graph = StateGraph(MetaAgentCoderState)

    graph.add_node("Test Designer", get_agent_coder_plus_tests_graph().compile())
    graph.add_node("Meta Programmer", get_agent_coder_plus_coder_graph().compile())
    graph.add_node("Chain of Thought Agent", AgentCoder())
    graph.add_node("Meta Controller", AgentMetaController())
    graph.add_node("Solution Evaluator", AgentSolutionEvaluator())

    graph.set_entry_point("Test Designer")
    graph.add_edge("Test Designer", "Meta Controller")

    graph.add_conditional_edges(
        "Meta Controller",
        router,
        {
            "MetaComplete": "Solution Evaluator",
            "MultiAgentContinue": "Meta Programmer",
            "SingleAgentContinue": "Chain of Thought Agent"
        }
    )

    graph.add_edge("Meta Programmer", "Meta Controller")
    graph.add_edge("Chain of Thought Agent", "Meta Controller")

    graph.add_edge("Solution Evaluator", END)

    return graph

if __name__ == "__main__":
    graph = get_meta_agent_coder_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
