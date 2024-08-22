import sys, os, json, random
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from data_classes.MATH.modeling.math_equivalence import is_equiv
from data_classes.MATH.modeling.dataset.util import last_boxed_only_string

import constants

class MathProblem():
    problem_statement: str # The problem_statement of the math problem
    problem_number: int # The number of the math problem correspoding to the original file name
    level: int # Difficulty level of the math problem can be from 1 to 5
    type: str # The type of the math problem
    justified_answer: str # The answer to the math problem with justification
    answer: str # The final boxed answer to the math problem

    def __init__(self, file_path: str):
        self._load_problem(file_path)
    
    def _load_problem(self, file_path: str):
        """
            Example file, 23.json:
            {
                "problem": "How many vertical asymptotes does the graph of $y=\\frac{2}{x^2+x-6}$ have?",
                "level": "Level 3",
                "type": "Algebra",
                "solution": "The denominator of the rational function factors into $x^2+x-6=(x-2)(x+3)$. Since the numerator is always nonzero, there is a vertical asymptote whenever the denominator is $0$, which occurs for $x = 2$ and $x = -3$.  Therefore, the graph has $\\boxed{2}$ vertical asymptotes."
            }
        """

        with open(file_path, "r") as f:
            data = json.load(f)
            self.problem_statement = data["problem"]
            self.level = self._parse_level(data["level"])
            self.type = data["type"]
            self.justified_answer = data["solution"]
            self.answer = last_boxed_only_string(self.justified_answer)
            self.problem_number = self._parse_problem_number(file_path.split("/")[-1].split(".")[0])
    
    def _parse_level(self, level: str):
        # Catch errors and display the error message
        try:
            return int(level.split()[-1])
        except:
            print(f"Error parsing level {level}")
            return 0
    
    def _parse_problem_number(self, problem_number: str):
        # Catch errors and display the error message
        try:
            return int(problem_number)
        except:
            print(f"Error parsing problem number {problem_number}")
            return 0
        
    def __str__(self) -> str:
        return f"MATH problem number {self.problem_number} of type {self.type} with level {self.level} and answer {self.answer}."
    
    def is_correct_answer(self, answer: str, verbose: bool = False) -> bool:
        # Check if the response is equivalent to the answer
        boxed_answer = last_boxed_only_string(answer)
        is_correct = is_equiv(boxed_answer, self.answer)
        if verbose:
            print(f"Level: {self.level} | Response: {boxed_answer} | Answer: {self.answer} | Is Correct: {is_correct}")
        return is_correct, boxed_answer, self.answer
    
    def get_id(self) -> str:
        return f"{self.type}_{self.problem_number}"
    
    

