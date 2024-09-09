import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from agent_coder.data_classes.AgentCoderState import AgentCoderState

from agent_coder.llm_agents.AgentTestGenerator import AgentTestGenerator
from agent_coder.llm_agents.AgentCoder import AgentCoder
from agent_coder.llm_agents.AgentTestExecutor import AgentTestExecutor
from agent_coder.llm_agents.AgentCodeRefiner import AgentCodeRefiner

def get_multi_agent_summarizer_graph():
    graph = StateGraph(AgentCoderState)

    graph.add_node("Test Designer", AgentTestGenerator())
    graph.add_node("Programmer", AgentCoder())   
    graph.add_node("Test Executor", AgentTestExecutor())
    graph.add_node("Programmer Refiner", AgentCodeRefiner())

    graph.set_entry_point("Test Designer")
    graph.add_edge("Test Designer", "Programmer")
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
    graph = get_multi_agent_summarizer_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
