import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from llm_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class Judgement(BaseModel):
    judgement: bool

    def __str__(self):
        return f"Judgement: {self.judgement}"

class AgentConditionJudge(MultiTurnLLMAgent):
    condition_judge_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionJudge"]
    condition_judge_summarization_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionJudgeSummarize"]

    def __init__(self):
        system_prompt = "You are a helpful AI assistant"
        super().__init__(system_prompt)

    def __call__(self, state: MACMState) -> Any:
        prompt_args = {
            "Known_condtions": state.verified_conditions,
            "condition_from_thinker": state.unverified_conditions
        }
        condition_judgement = self.user_prompt(self.condition_judge_prompt, prompt_args)
        summarized_condition_judegement = self.user_prompt(self.condition_judge_summarization_prompt, response_class=Judgement)
        if summarized_condition_judegement.judgement:
            if not state.verified_conditions:
                state.unverified_conditions = []
            state.verified_conditions.extend(state.unverified_conditions)
        print(f"Condition Judge Judgement: {summarized_condition_judegement.judgement}")

        return state
    

if __name__ == "__main__":  
    pass