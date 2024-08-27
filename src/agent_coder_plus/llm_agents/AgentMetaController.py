import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class AgentMetaController():

    def __call__(self, state) -> Any:
        print("\nIn AgentMetaMACMController at iteration ", state.current_meta_iterations+1, "\n")

        state.current_meta_iterations += 1
        if state.current_meta_iterations == state.n_multi_agent_iterations:
            if not state.multi_agent_completed:
                state.multi_agent_completed = True
                state.current_meta_iterations = 0
        
        # Check if there is a completed_method in the class
        if hasattr(state, "completed_method"):
            if state.completed_method in state.final_answers:
                state.final_answers[state.completed_method] += 1
            else:
                state.final_answers[state.completed_method] = 1

        return state.clean_state()
    

if __name__ == "__main__":  
    pass