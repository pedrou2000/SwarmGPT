import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from book_summarizer.llm_agents.simple_llm import SimpleLLMAgent
from generic_agents.MultiTurnLLMAgent import MultiTurnLLMAgent
import prompts
from typing import Any

from data_classes.MACMState import MACMState


class AgentIndividualMathSolver(MultiTurnLLMAgent):
    system_prompt: str = prompts.CHAIN_OF_THOUGHT_MATH_SOLVER["system_prompt"]
    chain_of_thought_prompt: str = prompts.CHAIN_OF_THOUGHT_MATH_SOLVER["user_prompt"]
    box_result_prompt: str = prompts.MACM_MATH_SOLVER["AgentStepsExecutionBoxResult"]

    def __init__(self):
        super().__init__(self.system_prompt)
        
    def __call__(self, state: MACMState) -> Any:
        print("In ChainOfThoughtMathSolver")
        prompt_args = {
            "problem": state.math_problem.problem_statement,
        }
        agent_response = self.user_prompt(self.chain_of_thought_prompt, prompt_args)
        box_result = self.user_prompt(self.box_result_prompt)

        state.final_answer = box_result
        print(f"Final Answer: {state.final_answer}")
        
        return state

if __name__ == "__main__":  
    math_solver = AgentIndividualMathSolver()
    problem_statement = "Solve the following equation: 2x + 3 = 7"
    print(math_solver(problem_statement))