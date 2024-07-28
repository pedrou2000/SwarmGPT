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



class AgentCoder(MultiTurnLLMAgent):
    system_prompt: str = prompts.AGENT_CODER["AgentCoder"]["system"]
    coder_prompt: str = prompts.AGENT_CODER["AgentCoder"]["user"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: AgentCoderState) -> Any:
        print("In AgentCoder")

        prompt_args = {
            "method_description": state.incomplete_method,
        }
        agent_response = self.user_prompt(self.coder_prompt, prompt_args)
        code = parse_python_code(agent_response)
        if code is None:
            print("No tests found in the response")
        state.completed_method = code
        self.reset_messages()
        return state
    

if __name__ == "__main__":  
    test_generator = AgentCoder()
    state = AgentCoderState(incomplete_method='def sum_x_y():\n')
    macm_state = test_generator(state)
    print(macm_state)
    print(macm_state.completed_method)
    

