import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class AgentMetaMACMController():

    def clean_state(self, state: MACMState) -> MACMState:
        # Clean the state
        state.verified_conditions = []
        state.unverified_conditions = []
        state.objectives = []
        state.steps = []
        state.final_answer = None
        return state

    def __call__(self, state: MACMState) -> Any:
        print("\n\n\nIn AgentMetaMACMController at iteration ", state.current_meta_iterations+1, "\n\n\n")

        state.current_meta_iterations += 1
        if state.current_meta_iterations == state.n_macm_iterations:
            if not state.macm_completed:
                state.macm_completed = True
                state.current_meta_iterations = 0
        
        if state.final_answer in state.final_answers:
            state.final_answers[state.final_answer] += 1
        else:
            state.final_answers[state.final_answer] = 1

        # Clean the state
        state = self.clean_state(state)

        return state
    

if __name__ == "__main__":  
    pass