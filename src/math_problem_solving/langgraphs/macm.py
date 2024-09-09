import sys
import os
sys.path.append(os.path.dirname(os.getcwd()))
from IPython.display import Image, display

from langgraph.graph import StateGraph, END

from data_classes.MACMState import MACMState
from math_problem_solving.llm_agents.AgentConditionAnalyzer import AgentConditionAnalyzer
from llm_agents.AgentConditionGenerator import AgentConditionGenerator
from llm_agents.AgentConditionJudge import AgentConditionJudge
from llm_agents.AgentAnswerReadyJudge import AgentAnswerReadyJudge
from llm_agents.AgentNumericalStepsGeneration import AgentNumericalStepsGeneration
from llm_agents.AgentStepsExecutor import AgentStepsExecutor

def get_macm_graph():
    graph = StateGraph(MACMState)

    graph.add_node("Objective Generator", AgentConditionAnalyzer())
    graph.add_node("Condition Generator", AgentConditionGenerator())
    graph.add_node("Condition Judge", AgentConditionJudge())
    graph.add_node("Answer Ready Judge", lambda state: state)
    graph.add_node("Numerical Steps Generator", AgentNumericalStepsGeneration())
    graph.add_node("Steps Executor", AgentStepsExecutor())

    graph.set_entry_point("Objective Generator")
    graph.add_edge("Objective Generator", "Condition Generator")
    graph.add_edge("Condition Generator", "Condition Judge")
    graph.add_edge("Condition Judge", "Answer Ready Judge")

    graph.add_conditional_edges(
        "Answer Ready Judge",
        AgentAnswerReadyJudge(),
        {
            "AnswerReady": "Numerical Steps Generator",
            "MaxIterationsReached": "Numerical Steps Generator",
            "AnswerNotReady": "Condition Generator"
        }
    )
    graph.add_edge("Numerical Steps Generator", "Steps Executor")
    graph.add_edge("Steps Executor", END)

    return graph

if __name__ == "__main__":
    graph = get_macm_graph()
    app = graph.compile()
    display(Image(app.get_graph(xray=True).draw_mermaid_png()))
