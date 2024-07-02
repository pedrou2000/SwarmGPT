import sys, os, json, random
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from data_classes.MATH.modeling.math_equivalence import is_equiv
from data_classes.MATH.modeling.dataset.util import last_boxed_only_string

import constants
from data_classes.MathProblem import MathProblem

class MathDataLoader():
    data_dir: str
    data: dict # Dictionary with keys the problem types and values lists of parsed MathProblem objects
    problem_types: list # List of problem types: ["algebra", ...]
    n_total_problems: int # Total number of problems loaded

    def __init__(self, data_dir: str = "../../data/datasets/MATH/test/"):
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
    
    def get_problem(self, type:str = "algebra", problem_number:int = 265) -> MathProblem:
        # Get a problem by type and number
        for problem in self.data[type]:
            if problem.problem_number == problem_number:
                return problem
        print(f"Problem {problem_number} of type {type} not found")
        return None
    
    def test_random_problems(self, agent: callable, n_problems: int = 10, level: int = None, verbose: bool = False) -> float:
        # Test the agent on n_problems and return the accuracy
        n_correct = 0
        for i in range(n_problems):
            problem = self.get_random_problem(level=level)
            response = agent(problem.problem_statement)
            if problem.is_correct_answer(response):
                n_correct += 1
        result = n_correct/n_problems  
        if verbose:
            print(f"Agent accuracy on {n_problems} problems of level {level}: {result}")

        return result


if __name__ == "__main__":
    mdl = MathDataLoader(data_dir=constants.MATH_DATASET_DIR)
    print("Loaded Math Data Loader with Problem Types: ", mdl.problem_types)   
    random_problem = mdl.get_random_problem()
    print("Random Problem: ", random_problem) 