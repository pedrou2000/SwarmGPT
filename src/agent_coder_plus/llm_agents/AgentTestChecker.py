import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))))

from generic_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.AgentCoderPlusCoderState import AgentCoderPlusCoderState
from human_eval_utils import parse_python_code

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List, Annotated

class TestCheckerOutput(BaseModel):
    n_total_tests: Annotated[int, "Total number of tests"]
    n_passed_tests: Annotated[int, "Number of tests that passed"]
    feedback: Annotated[str, "Feedback on how to fix the tests"]
    # refine_else_restart: Annotated[bool, "Whether to refine the tests or else restart the process"]


class AgentTestChecker(MultiTurnLLMAgent):
    system_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestChecker"]["system"]
    test_checker_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestChecker"]["user"]

    def __init__(self):
        # Pass the system_prompt specific to AgentTestExecutor to the base class
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: AgentCoderPlusCoderState) -> Any:
        print("In AgentTestChecker")

        prompt_args = {
            "method_description": state.incomplete_method,
            "generated_tests": state.generated_tests
        }
        output = self.user_prompt(self.test_checker_prompt, prompt_args, response_class=TestCheckerOutput)
        self.reset_messages()

        state.feedback = output.feedback

        if output.n_total_tests == 0:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n zero tests executed \n {state.generated_tests} \n\n\n\n\n\n\n\n\n\n\n")
        proportion_tests_passed = output.n_passed_tests / output.n_total_tests
        state.tests_passed = True if proportion_tests_passed >= state.passed_tests_threshold else False
         # state.refine_else_restart = output.refine_else_restart

        if not state.current_iterations:
            state.current_iterations = 1
        else:
            state.current_iterations += 1

        return state
    

if __name__ == "__main__":  
    test_executor = AgentTestChecker()
    state = AgentCoderState(completed_method='def sum_x_y():\n    return x + y\n', generated_tests='assert sum_x_y(1, 2) == 3')
    macm_state = test_executor(state)
    macm_state = test_executor(state)
    