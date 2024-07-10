import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from llm_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Any, List, Annotated

class AgentStepsExecutor(MultiTurnLLMAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["executor"]
    steps_exection_prompt: str = prompts.MACM_MATH_SOLVER["AgentStepsExecution"]
    box_result_prompt: str = prompts.MACM_MATH_SOLVER["AgentStepsExecutionBoxResult"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)


    def __call__(self, state: MACMState) -> Any:
        print("In AgentStepsExecutor")
        self.reset_messages()
        prompt_args = {
            "Conditions": state.verified_conditions,
            "Objective": state.objectives, 
            "Steps": state.steps
        }
        numerical_steps = self.user_prompt(self.steps_exection_prompt, prompt_args=prompt_args, response_class=None)
        box_result = self.user_prompt(self.box_result_prompt)

        state.final_answer = box_result

        print(f"Final Answer: {state.final_answer}")

        return state
    