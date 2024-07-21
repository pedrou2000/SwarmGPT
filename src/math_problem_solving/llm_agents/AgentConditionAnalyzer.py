import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from data_classes.MACMState import MACMState
from data_classes.MathProblem import MathProblem    

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class AgentConditionAnalyzerResponse(BaseModel):
    conditions: List[str]
    objectives: List[str]



class AgentConditionAnalyzer(CodeInterpreterAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["thinker"]
    condition_analyzer_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionAnalyzer"]
    parser_prompt: str = prompts.MACM_MATH_SOLVER["AgentResponseParser"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: MACMState) -> Any:
        print("In AgentConditionAnalyzer")

        prompt_args = {
            "Question": state.math_problem.problem_statement,
        }
        agent_response = self.user_prompt(self.condition_analyzer_prompt, prompt_args)
        structured_response = self.structured_output(AgentConditionAnalyzerResponse, self.parser_prompt, str(agent_response))

        state.verified_conditions = structured_response.conditions
        state.objectives = structured_response.objectives
        print(f"{len(state.verified_conditions)} Conditions: \n{state.verified_conditions}")
        print(f"{len(state.objectives)} Objectives: \n{state.objectives}")
        return state
    

if __name__ == "__main__":  
    math_solver = AgentConditionAnalyzer()
    problem_statement = "Solve the following equation: 2x + 3 = 7"
    math_problem = MathProblem(file_path="0.json")
    macm_state = MACMState(math_problem=math_problem, max_iterations=1)
    print(math_solver(macm_state))