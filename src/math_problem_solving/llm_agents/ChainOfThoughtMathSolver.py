import sys, os
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from book_summarizer.llm_agents.simple_llm import SimpleLLMAgent
import prompts
from typing import Any


class ChainOfThoughtMathSolver(SimpleLLMAgent):
    def __init__(self):
        system_prompt = prompts.CHAIN_OF_THOUGHT_MATH_SOLVER["system_prompt"]
        user_prompt = prompts.CHAIN_OF_THOUGHT_MATH_SOLVER["user_prompt"]
        response_class = None
        super().__init__(system_prompt, user_prompt, response_class)
        
    def __call__(self, problem_statement) -> Any:
        agent_response = self.agent.invoke({"problem":  problem_statement})
        return agent_response.content
    

if __name__ == "__main__":  
    math_solver = ChainOfThoughtMathSolver()
    problem_statement = "Solve the following equation: 2x + 3 = 7"
    print(math_solver(problem_statement))