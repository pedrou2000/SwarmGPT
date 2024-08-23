import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class Judgement(BaseModel):
    judgement: bool

    def __str__(self):
        return f"Judgement: {self.judgement}"

class AgentConditionJudge(CodeInterpreterAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["judge"]
    condition_judge_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionJudge"]
    condition_judge_summarization_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionJudgeSummarize"]
    parser_prompt: str = prompts.MACM_MATH_SOLVER["AgentResponseParser"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)

    def __call__(self, state: MACMState) -> Any:
        print("In AgentConditionJudge")
        prompt_args = {
            "Known_condtions": state.verified_conditions,
            "condition_from_thinker": state.unverified_conditions
        }
        condition_judgement = self.user_prompt(self.condition_judge_prompt, prompt_args)
        summarized_condition_judegement = self.user_prompt(self.condition_judge_summarization_prompt)
        summarized_condition_judegement = self.structured_output(Judgement, self.parser_prompt, summarized_condition_judegement)
        if summarized_condition_judegement.judgement:
            if not state.verified_conditions:
                state.unverified_conditions = []
            state.verified_conditions.extend(state.unverified_conditions)
        state.unverified_conditions = []
        # print(f"Condition Judge Judgement: {summarized_condition_judegement.judgement}")

        return state
    

if __name__ == "__main__":  
    pass