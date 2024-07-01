import os, json, random

from MATH.modeling.math_equivalence import is_equiv
from MATH.modeling.dataset.util import last_boxed_only_string

class MathProblem():
    question: str # The question of the math problem
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
            self.question = data["problem"]
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
        return is_correct

class MathDataLoader():
    data_dir: str
    data: dict # Dictionary with keys the problem types and values lists of parsed MathProblem objects
    problem_types: list # List of problem types: ["algebra", ...]
    n_total_problems: int # Total number of problems loaded

    def __init__(self, data_dir: str = "../../../data/datasets/MATH/test/"):
        self.data_dir = data_dir
        self._load_data()

    def _load_data(self):
        # The data is a dictionary with keys the problem types and values dictionaries with keys the problem numbers 
        # and values the problem data
        
        if not os.path.exists(self.data_dir):
            print(f"Folder {self.data_dir} does not exist")
        
        self.data = {}
        self.problem_types = []

        for problem_type in os.listdir(self.data_dir):
            self.data[problem_type] = []
            self.problem_types.append(problem_type)

            for problem_file in os.listdir(os.path.join(self.data_dir, problem_type)):
                problem_dir = os.path.join(self.data_dir, problem_type, problem_file)
                math_problem = MathProblem(problem_dir)
                self.data[problem_type].append(math_problem)
        
        self.n_total_problems = sum([len(self.data[problem_type]) for problem_type in self.problem_types])
        print(f"Loaded {self.n_total_problems} math problems from {len(self.problem_types)} problem types") 

    def get_random_problem(self, level: int = None, problem_type: str = None) -> MathProblem:
        # Get a random problem from the data
        if problem_type is  None:
            problem_type = random.choice(self.problem_types)
        if level is not None:
            problems_of_level = [problem for problem in self.data[problem_type] if problem.level == level]
            problem = random.choice(problems_of_level)
        else:
            problem = random.choice(self.data[problem_type])
        return problem



if __name__ == "__main__":
    data_dir="../../../data/datasets/MATH/test/"
    mdl = MathDataLoader(data_dir=data_dir)
    print("Loaded Math Data Loader with Problem Types: ", mdl.problem_types)   
    random_problem = mdl.get_random_problem()
    print("Random Problem: ", random_problem) 