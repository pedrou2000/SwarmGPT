import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from book_summarizer.llm_agents.simple_llm import SimpleLLMAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class AgentConditionAnalyzerResponse(BaseModel):
    conditions: List[str]
    objectives: List[str]



class AgentConditionAnalyzer(SimpleLLMAgent):
    def __init__(self):
        system_prompt = "You are a helpful AI assistant"
        user_prompt = prompts.MACM_MATH_SOLVER["AgentConditionAnalyzer"]
        response_class = AgentConditionAnalyzerResponse
        super().__init__(system_prompt, user_prompt, response_class)
        
    def __call__(self, state: MACMState) -> Any:
        problem_statement = state.math_problem.problem_statement
        agent_response = self.agent.invoke({"Question":  problem_statement})
        state.unverified_conditions = agent_response.conditions
        state.objectives = agent_response.objectives
        print(f"Conditions: \n{state.unverified_conditions}")
        print(f"Objectives: \n{state.objectives}")
        return state
    

if __name__ == "__main__":  
    math_solver = AgentConditionAnalyzer()
    problem_statement = "Solve the following equation: 2x + 3 = 7"
    print(math_solver(problem_statement))