import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from book_summarizer.llm_agents.simple_llm import SimpleLLMAgent
from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts
from typing import Any


class ChainOfThoughtMathSolver(CodeInterpreterAgent):
    system_prompt: str = prompts.CHAIN_OF_THOUGHT_MATH_SOLVER["system_prompt"]
    chain_of_thought_prompt: str = prompts.CHAIN_OF_THOUGHT_MATH_SOLVER["user_prompt"]

    def __init__(self):
        super().__init__(self.system_prompt)
        
    def __call__(self, problem_statement) -> Any:
        print("In ChainOfThoughtMathSolver")
        prompt_args = {
            "problem": problem_statement,
        }
        agent_response = self.user_prompt(self.chain_of_thought_prompt, prompt_args)
        return agent_response
    

if __name__ == "__main__":  
    math_solver = ChainOfThoughtMathSolver()
    problem_statement = "Solve the following equation: 2x + 3 = 7"
    print(math_solver(problem_statement))