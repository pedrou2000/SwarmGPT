import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from agent_coder_plus.data_classes.AgentCoderPlusCoderState import AgentCoderPlusCoderState

from llm_agents.AgentCoder import AgentCoder
from llm_agents.AgentTestExecutor import AgentTestExecutor
from llm_agents.AgentCodeRefiner import AgentCodeRefiner

from data_classes.AgentCoderPlusCoderState import AgentCoderPlusCoderState

def get_agent_coder_plus_coder_graph():
    graph = StateGraph(AgentCoderPlusCoderState)

    graph.add_node("Programmer", AgentCoder())   
    graph.add_node("Test Executor", AgentTestExecutor())
    graph.add_node("Programmer Refiner", AgentCodeRefiner())

    graph.set_entry_point("Programmer")
    graph.add_edge("Programmer", "Test Executor")

    graph.add_conditional_edges(
        "Test Executor",
        lambda state:  "TestsPassed" if state.tests_passed else ("MaxIterations" if state.current_iterations >= state.max_iterations else "TestsFailed"),
        {
            "TestsPassed": END,
            "MaxIterations": END,
            "TestsFailed": "Programmer Refiner"
        }
    )
    
    graph.add_edge("Programmer Refiner", "Test Executor")

    return graph


if __name__ == "__main__":
    graph = get_agent_coder_plus_coder_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
