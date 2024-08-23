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

class AgentAnswerReadyJudge(CodeInterpreterAgent):
    system_prompt: str = prompts.MACM_MATH_SOLVER["system_prompts"]["judge"]
    answer_ready_prompt: str = prompts.MACM_MATH_SOLVER["AgentAnwerReadyJudge"]
    anwer_ready_summarization_prompt: str = prompts.MACM_MATH_SOLVER["AgentAnswerReadyJudgeSummarize"]
    parser_prompt: str = prompts.MACM_MATH_SOLVER["AgentResponseParser"]

    def __init__(self):
        super().__init__(system_prompt=self.system_prompt)

    def __call__(self, state: MACMState) -> Any:
        print("In AgentAnswerReadyJudge")

        prompt_args = {
            "Known_condtions": state.verified_conditions,
            "Objective": state.objectives
        }
        answer_ready_judgement = self.user_prompt(self.answer_ready_prompt, prompt_args)
        # print("Answer Ready Judgement: ", answer_ready_judgement)
        summarized_answer_ready_judgement = self.user_prompt(self.anwer_ready_summarization_prompt)
        summarized_answer_ready_judgement = self.structured_output(Judgement, self.parser_prompt, summarized_answer_ready_judgement)
        # print(f"Answer Ready Judgement: {summarized_answer_ready_judgement.judgement}")

        if summarized_answer_ready_judgement.judgement:
            response = "AnswerReady"
        elif state.current_iterations == state.max_iterations:
            response = "MaxIterationsReached"
        else:
            response = "AnswerNotReady"

        return response
    

if __name__ == "__main__":  
    pass