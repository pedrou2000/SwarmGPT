import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))))

from generic_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List, Annotated

class TestCheckerOutput(BaseModel):
    n_total_tests: Annotated[int, "Total number of tests"]
    n_passed_tests: Annotated[int, "Number of tests that passed"]
    feedback: Annotated[str, "Feedback on how to fix the tests"]
    # refine_else_restart: Annotated[bool, "Whether to refine the tests or else restart the process"]


class AgentTestChecker(MultiTurnLLMAgent):
    system_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentTestChecker"]["system"]
    test_checker_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentTestChecker"]["user"]

    def __init__(self):
        # Pass the system_prompt specific to AgentTestExecutor to the base class
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state) -> Any:
        print("In AgentTestChecker")

        prompt_args = {
            "math_problem": state.math_problem.problem_statement,
            "generated_tests": state.generated_tests
        }
        output = self.user_prompt(self.test_checker_prompt, prompt_args, response_class=TestCheckerOutput)
        self.reset_messages()

        state.feedback = output.feedback

        proportion_tests_passed = output.n_passed_tests / output.n_total_tests
        if proportion_tests_passed >= state.passed_tests_threshold:
            state.tests_passed = True  
            state.current_iterations = -1
        else:
            state.tests_passed = False

        if not state.current_iterations:
            state.current_iterations = 1
        else:
            state.current_iterations += 1

        return state
    

if __name__ == "__main__":  
    test_executor = AgentTestChecker()
    