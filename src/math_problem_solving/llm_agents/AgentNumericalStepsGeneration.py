import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from llm_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Any, List, Annotated

class NumericalSteps(BaseModel):
    steps: Annotated[List[str], Field(description="List of steps to solve the math problem")]

class AgentNumericalStepsGeneration(MultiTurnLLMAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["thinker"]
    numerical_steps_generation_prompt: str = prompts.MACM_MATH_SOLVER["AgentNumericalStepsGeneration"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)


    def __call__(self, state: MACMState) -> Any:
        print("In AgentNumericalStepsGeneration")
        self.reset_messages()
        prompt_args = {
            "Known_conditions": state.verified_conditions,
            "Objective": state.objectives
        }
        numerical_steps = self.user_prompt(self.numerical_steps_generation_prompt, response_class=NumericalSteps)

        state.steps = numerical_steps.steps

        print(f"Final Steps to solve the problem: {state.steps}")

        return state
    