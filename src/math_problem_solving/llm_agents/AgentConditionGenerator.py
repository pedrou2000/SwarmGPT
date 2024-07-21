import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Any, List, Annotated

class SummarizedCondition(BaseModel):
    preconditions: Annotated[List[str], Field(description="List of preconditions of the new derived condition")]
    derived_condition: Annotated[str, Field(description="Newly derived condition from the preconditions")]
    reasoning: Annotated[str, Field(description="Reasoning for the derived condition")]

    def __str__(self) -> str:
        return f"Based on the known conditions: {self.preconditions}, we can derive the following condition: {self.derived_condition}\n Resoning: {self.reasoning}"


class AgentConditionGenerator(CodeInterpreterAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["thinker"]
    condition_generation_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionGeneratorGenerate"]
    condition_summarization_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionGeneratorSummarize"]
    parser_prompt: str = prompts.MACM_MATH_SOLVER["AgentResponseParser"]

    def __init__(self):
        super().__init__(self.system_prompt)


    def __call__(self, state: MACMState) -> Any:
        print("In AgentConditionGenerator")
        prompt_args = {
            "Known_conditions": state.verified_conditions,
            "Objective": state.objectives
        }
        new_condition = self.user_prompt(self.condition_generation_prompt, prompt_args)
        summarized_condition = self.user_prompt(self.condition_summarization_prompt)
        parsed_condition = self.structured_output(SummarizedCondition, self.parser_prompt, summarized_condition)

        if not state.unverified_conditions:
            state.unverified_conditions = []
        state.unverified_conditions.append(parsed_condition.derived_condition)
        # print(f"New condition: {new_condition}")
        print(f"Summarized condition: {parsed_condition}")

        return state
    