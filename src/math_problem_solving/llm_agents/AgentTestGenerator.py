import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.MathDataLoader import MathDataLoader

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List
import constants


class AgentTestGenerator(MultiTurnLLMAgent):
    system_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentTestGenerator"]["system"]
    test_generator_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentTestGenerator"]["user"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state) -> Any:
        print("In AgentTestGenerator")

        prompt_args = {
            "math_problem": state.math_problem.problem_statement,
        }
        agent_response = self.user_prompt(self.test_generator_prompt, prompt_args)
        # tests = parse_python_code(agent_response)
        # if tests is None:
            # print("No tests found in the response")
        
        # print("Generated tests: \n", tests)
        state.generated_tests = agent_response
        # print("System prompt: \n", self.system_prompt)
        # print("Generated tests: \n", state.generated_tests)

        self.reset_messages()
        return state

class State(BaseModel):
    math_problem: Any
    generated_tests: str

if __name__ == "__main__":  
    test_generator = AgentTestGenerator()

    math_data_loader = MathDataLoader(data_dir=constants.MATH_DATASET_DIR)
    random_problem = math_data_loader.get_problem(type="precalculus", problem_number=1098)

    state = State(math_problem=random_problem, generated_tests="")
    macm_state = test_generator(state)
    print(macm_state.generated_tests)
    