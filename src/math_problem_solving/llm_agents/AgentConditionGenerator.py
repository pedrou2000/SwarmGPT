import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from llm_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from data_classes.MACMState import MACMState

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List

class AgentConditionGenerator(MultiTurnLLMAgent):
    condition_generation_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionGeneratorGenerate"]
    condition_summarization_prompt: str = prompts.MACM_MATH_SOLVER["AgentConditionGeneratorSummarize"]

    def __init__(self):
        system_prompt = "You are a helpful AI assistant"
        super().__init__(system_prompt)

    def test(self, message: str):
        return self.user_prompt(message)
    
    def test_2(self):
        prompt_template = "Solve the following math problem: {problem}"
        prompt_args = {"problem": "Solve the following equation: 2x + 3 = 7"}
        return self.user_prompt(prompt_template, prompt_args)


    def __call__(self, state: MACMState) -> Any:
        prompt_args = {
            "Known_conditions": state.verified_conditions,
            "Objective": state.objectives
        }
        new_condition = self.user_prompt(self.condition_generation_prompt, prompt_args)
        summarized_condition = self.user_prompt(self.condition_summarization_prompt)
        if not state.unverified_conditions:
            state.unverified_conditions = []
        state.unverified_conditions.append(summarized_condition)
        # print(f"New condition: {new_condition}")
        print(f"Summarized condition: {summarized_condition}")

        return state
    

if __name__ == "__main__":  
    math_solver = AgentConditionGenerator()
    print(math_solver.test_2())

    state = MACMState(
        math_problem="Solve the following equation: 2x + 3 = 7",
        verified_conditions=[],
        unverified_conditions=[],
        objectives=["Solve the following equation: 2x + 3 = 7"]
    )
    print('---')
    print(math_solver(state))