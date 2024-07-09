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

class AgentAnswerReadyJudge(MultiTurnLLMAgent):
    answer_ready_prompt: str = prompts.MACM_MATH_SOLVER["AgentAnwerReadyJudge"]
    anwer_ready_summarization_prompt: str = prompts.MACM_MATH_SOLVER["AgentAnswerReadyJudgeSummarize"]

    def __init__(self):
        system_prompt = "You are a helpful AI assistant"
        super().__init__(system_prompt)

    def __call__(self, state: MACMState) -> Any:
        prompt_args = {
            "Known_condtions": state.verified_conditions,
            "Objective": state.objectives
        }
        answer_ready_judgement = self.user_prompt(self.answer_ready_prompt, prompt_args)
        print("Answer Ready Judgement: ", answer_ready_judgement)
        summarized_answer_ready_judgement = self.user_prompt(self.anwer_ready_summarization_prompt, response_class=Judgement)
        print(f"Answer Ready Judgement: {summarized_answer_ready_judgement.judgement}")

        if summarized_answer_ready_judgement.judgement:
            response = "AnswerReady"
        else:
            response = "AnswerNotReady"

        return response
    

if __name__ == "__main__":  
    pass