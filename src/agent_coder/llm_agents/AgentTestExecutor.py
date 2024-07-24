import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from agent_coder.data_classes.AgentCoderState import AgentCoderState
from human_eval_utils import parse_python_code

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class TestExecutorOutput(BaseModel):
    tests_passed: bool
    feedback: str



class AgentTestExecutor(CodeInterpreterAgent):
    system_prompt: str = prompts.AGENT_CODER["AgentTestExecutor"]["system"]
    test_executor_prompt: str = prompts.AGENT_CODER["AgentTestExecutor"]["user"]
    parser_system_prompt: str = prompts.AGENT_CODER["AgentTestExecutor"]["parser_system"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: AgentCoderState) -> Any:
        print("In AgentTestExecutor")

        prompt_args = {
            "completed_method": state.completed_method,
            "test_cases": state.generated_tests
        }
        agent_response = self.user_prompt(self.test_executor_prompt, prompt_args)
        self.delete_all_messages()

        input_to_parse = state.completed_method + state.generated_tests + agent_response
        output = self.structured_output(response_class=TestExecutorOutput, system_prompt=self.parser_system_prompt, message=input_to_parse)

        state.tests_passed = output.tests_passed
        state.feedback = output.feedback

        if not state.current_iterations:
            state.current_iterations = 1
        else:
            state.current_iterations += 1
        print(f"Current iterations: {state.current_iterations}")
        print(f"Tests passed: {state.tests_passed}\nFeedback: \n{state.feedback}")




        return state
    

if __name__ == "__main__":  
    test_executor = AgentTestExecutor()
    state = AgentCoderState(completed_method='def sum_x_y():\n    return x + y\n', generated_tests='assert sum_x_y(1, 2) == 3')
    macm_state = test_executor(state)
    