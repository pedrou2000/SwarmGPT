import sys
import os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END
from human_eval_utils import load_human_eval
from utils import print_dict

from data_classes.AgentCoderPlusTestsState import AgentCoderPlusTestsState

from llm_agents.AgentTestGenerator import AgentTestGenerator
from llm_agents.AgentTestChecker import AgentTestChecker
from llm_agents.AgentTestRefiner import AgentTestRefiner

def tests_router(state: AgentCoderPlusTestsState):
    if state.tests_passed:
        return "TestsReady"
    elif state.current_iterations >= state.max_iterations / 2:
        return "MaxIterations"
    else:
        return "RefineTests"

def get_agent_coder_plus_tests_graph():
    graph = StateGraph(AgentCoderPlusTestsState)

    graph.add_node("Test Generator", AgentTestGenerator())
    graph.add_node("Test Checker", AgentTestChecker())
    graph.add_node("Test Refiner", AgentTestRefiner())

    graph.set_entry_point("Test Generator")
    graph.add_edge("Test Generator", "Test Checker")
    graph.add_conditional_edges(
        "Test Checker",
        tests_router,
        {
            "TestsReady": END,
            "MaxIterations": END,
            "RefineTests": "Test Refiner",
        }
    )
    graph.add_edge("Test Refiner", "Test Checker")

    return graph


if __name__ == "__main__":
    graph = get_agent_coder_plus_tests_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))

    dataset = load_human_eval()
    task = dataset[32]
    
    state = AgentCoderPlusTestsState(incomplete_method=task["prompt"], max_iterations=3)
    app = graph.compile()

    for event in app.stream({"incomplete_method":task["prompt"], "max_iterations":3}):
        print_dict(event)
                  
