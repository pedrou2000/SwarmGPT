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

    graph.add_node("Test Generator", AgentTestGenerator())
    graph.add_node("Coder", AgentCoder())   
    graph.add_node("Test Executor", AgentTestExecutor())
    graph.add_node("Code Refiner", AgentCodeRefiner())

    graph.set_entry_point("Test Generator")
    graph.add_edge("Test Generator", "Coder")
    graph.add_edge("Coder", "Test Executor")

    graph.add_conditional_edges(
        "Test Executor",
        lambda state:  "CodeReady" if state.tests_passed else ("MaxIterations" if state.current_iterations >= state.max_iterations else "CodeNotReady"),
        {
            "CodeReady": END,
            "MaxIterations": END,
            "CodeNotReady": "Code Refiner"
        }
    )
    
    graph.add_edge("Code Refiner", "Test Executor")

    return graph

if __name__ == "__main__":
    graph = get_multi_agent_summarizer_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
