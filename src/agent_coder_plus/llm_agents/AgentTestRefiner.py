import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from agent_coder.data_classes.AgentCoderState import AgentCoderState
from human_eval_utils import parse_python_code

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List



class AgentTestRefiner(MultiTurnLLMAgent):
    system_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestRefiner"]["system"]
    coder_prompt: str = prompts.AGENT_CODER_PLUS["AgentTestRefiner"]["user"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: AgentCoderState) -> Any:
        print("In AgentTestRefiner")

        prompt_args = {
            "method_description": state.incomplete_method,
            "generated_tests": state.generated_tests,
            "feedback": state.feedback
        }
        agent_response = self.user_prompt(self.coder_prompt, prompt_args)
        # print(agent_response)
        code = parse_python_code(agent_response)
        if code is None:
            print("No tests found in the response")
        state.generated_tests = code
        self.reset_messages()
        return state
    

if __name__ == "__main__":  
    test_generator = AgentTestRefiner()
    state = AgentCoderState(completed_method='def sum_x_y():\n    return x - y\n', 
                            feedback='The code does not pass the tests because the code is performing subtraction instead of addition')
    macm_state = test_generator(state)
    

