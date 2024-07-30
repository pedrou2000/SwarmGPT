import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd()))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.getcwd())))))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from data_classes.AgentCoderPlusCoderState import AgentCoderPlusCoderState
from human_eval_utils import parse_python_code

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class TestExecutorOutput(BaseModel):
    n_total_tests: int
    n_passed_tests: int
    feedback: str

class AgentTestExecutor(CodeInterpreterAgent):
    system_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestExecutor"]["system"]
    test_executor_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestExecutor"]["user"]
    parser_system_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestExecutor"]["parser_system"]

    def __init__(self):
        # Pass the system_prompt specific to AgentTestExecutor to the base class
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: AgentCoderPlusCoderState) -> Any:
        print("In AgentTestExecutor, with thread id: ", self.thread)

        prompt_args = {
            "completed_method": state.completed_method,
            "test_cases": state.generated_tests
        }
        agent_response = self.user_prompt(self.test_executor_prompt, prompt_args)
        self.delete_all_messages()

        input_to_parse = state.completed_method + state.generated_tests + agent_response
        output = self.structured_output(response_class=TestExecutorOutput, system_prompt=self.parser_system_prompt, message=input_to_parse)

        proportion_tests_passed = output.n_passed_tests / output.n_total_tests
        state.tests_passed = True if proportion_tests_passed >= state.passed_tests_threshold else False

        state.feedback = output.feedback

        if not state.current_iterations:
            state.current_iterations = 1
        else:
            state.current_iterations += 1
        print(f"Current iterations: {state.current_iterations}")
        print(f"Tests passed: {state.tests_passed}. Proportion tests passed: {proportion_tests_passed}\nFeedback: \n{state.feedback}")

        self.delete_all_messages()
        return state
    

if __name__ == "__main__":  
    test_executor = AgentTestExecutor()
    state = AgentCoderState(completed_method='def sum_x_y():\n    return x + y\n', generated_tests='assert sum_x_y(1, 2) == 3')
    macm_state = test_executor(state)
    macm_state = test_executor(state)
    