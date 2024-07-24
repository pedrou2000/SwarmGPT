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



class AgentCodeRefiner(MultiTurnLLMAgent):
    system_prompt: str = prompts.AGENT_CODER["AgentCodeRefiner"]["system"]
    coder_prompt: str = prompts.AGENT_CODER["AgentCodeRefiner"]["user"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state: AgentCoderState) -> Any:
        print("In AgentCodeRefiner")

        prompt_args = {
            "completed_method": state.completed_method,
            "feedback": state.feedback
        }
        agent_response = self.user_prompt(self.coder_prompt, prompt_args)
        # print(agent_response)
        code = parse_python_code(agent_response)
        if code is None:
            print("No tests found in the response")
        state.completed_method = code
        return state
    

if __name__ == "__main__":  
    test_generator = AgentCodeRefiner()
    state = AgentCoderState(completed_method='def sum_x_y():\n    return x - y\n', 
                            feedback='The code does not pass the tests because the code is performing subtraction instead of addition')
    macm_state = test_generator(state)
    

