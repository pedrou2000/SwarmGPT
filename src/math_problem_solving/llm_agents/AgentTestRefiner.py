import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from human_eval_utils import parse_python_code

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List



class AgentTestRefiner(MultiTurnLLMAgent):
    system_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentTestRefiner"]["system"]
    refiner_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentTestRefiner"]["user"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state) -> Any:
        print("In AgentTestRefiner")

        prompt_args = {
            "math_problem": state.math_problem.problem_statement,
            "generated_tests": state.generated_tests,
            "feedback": state.feedback
        }
        agent_response = self.user_prompt(self.refiner_prompt, prompt_args)
        # print(agent_response)
        # code = parse_python_code(agent_response)
        # if code is None:
        #     print("No tests found in the response")
        state.generated_tests = agent_response
        self.reset_messages()
        return state
    

if __name__ == "__main__":  
    test_refiner = AgentTestRefiner()
    

