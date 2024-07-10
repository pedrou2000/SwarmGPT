import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from llm_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class AgentConditionAnalyzerResponse(BaseModel):
    conditions: List[str]
    objectives: List[str]



class AgentConditionAnalyzer(MultiTurnLLMAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["thinker"]
    condition_analyzer_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionAnalyzer"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: MACMState) -> Any:
        print("In AgentConditionAnalyzer")

        self.reset_messages()
        prompt_args = {
            "Question": state.math_problem.problem_statement,
        }
        agent_response = self.user_prompt(self.condition_analyzer_prompt, prompt_args, response_class=AgentConditionAnalyzerResponse)

        state.verified_conditions = agent_response.conditions
        state.objectives = agent_response.objectives
        print(f"Conditions: \n{state.verified_conditions}")
        print(f"Objectives: \n{state.objectives}")
        return state
    

if __name__ == "__main__":  
    math_solver = AgentConditionAnalyzer()
    problem_statement = "Solve the following equation: 2x + 3 = 7"
    print(math_solver(problem_statement))