import concurrent.futures
import sys, os, json, random, time, pickle
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
    
    def get_several_random_problems(self, n_problems: int = 1,  level: int = None, problem_type: str = None) -> MathProblem:
        # Get a random problem from the data
        if problem_type is  None:
            problem_type = random.choice(self.problem_types)
        if level is not None:
            problems_of_level = [problem for problem in self.data[problem_type] if problem.level == level]
            selected_problems = random.sample(problems_of_level, n_problems)
        else:
            selected_problems = random.sample(self.data[problem_type], n_problems)  
        return selected_problems
    
    def get_random_problems_balanced(self, n_problems_per_level_and_type: int = 2) -> list:
        # Get a balanced set of random problems
        problems = []
        for problem_type in self.problem_types:
            for level in range(1, 6):
                problems.extend(self.get_several_random_problems(n_problems=n_problems_per_level_and_type, level=level, problem_type=problem_type))
                
        return problems
    
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

    def get_random_problems(self, proportion: float = None, n_problems: int = None, level: int = None) -> list:
        """
        Get a random subset of problems from the dataset.

        :param proportion: The proportion of the total number of problems to return (between 0 and 1).
        :param n_problems: The exact number of problems to return.
        :param level: The difficulty level of the problems to return (optional).
        :return: A list of MathProblem objects.
        """
        # Ensure either proportion or n_problems is specified, but not both
        if proportion is not None and n_problems is not None:
            raise ValueError("Specify either proportion or n_problems, not both.")
        
        if proportion is not None:
            if not (0 < proportion <= 1):
                raise ValueError("Proportion must be a value between 0 and 1.")
            # Count the problems based on the level if specified
            if level is not None:
                level_problems = [problem for problem in self.get_all_problems() if problem.level == level]
                n_problems = int(proportion * len(level_problems))
            else:
                n_problems = int(proportion * self.n_total_problems)
        
        if n_problems is None:
            raise ValueError("You must specify either proportion or n_problems.")

        # Filter by level if specified
        if level is not None:
            all_problems = [problem for problem in self.get_all_problems() if problem.level == level]
            if n_problems > len(all_problems):
                raise ValueError(f"Requested {n_problems} problems, but only {len(all_problems)} are available at level {level}.")
        else:
            all_problems = self.get_all_problems()
            if n_problems > self.n_total_problems:
                raise ValueError(f"Requested {n_problems} problems, but only {self.n_total_problems} are available.")
        
        return random.sample(all_problems, n_problems)
    
    def save_problems(self, problems: list, save_path: str):
        """
        Save a list of MathProblem objects to a file.

        :param problems: The list of MathProblem objects to save.
        :param save_path: The file path where the problems should be saved.
        """
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
        with open(save_path, 'wb') as file:
            pickle.dump(problems, file)
    
    @staticmethod
    def load_problems(load_path: str) -> list:
        """
        Load a list of MathProblem objects from a file.

        :param load_path: The file path from which to load the problems.
        :return: A list of MathProblem objects.
        """
        with open(load_path, 'rb') as file:
            problems = pickle.load(file)
        return problems

    def get_all_problems(self) -> list:
        """
        Get a list of all problems across all problem types.
        
        :return: A list of all MathProblem objects.
        """
        all_problems = []
        for problem_type in self.problem_types:
            all_problems.extend(self.data[problem_type])
        return all_problems


    def test_math_task(self, agent: callable, math_problem: MathProblem, n_attempts: int = 5):
        n_attempt = 0
        while n_attempt < n_attempts:
            try:
                response = agent(math_problem)
                break
            except Exception as e:
                print(f"Error in test_math_task: {e}")
                time.sleep(10)
                n_attempt += 1
        is_correct, agent_answer, real_answer = math_problem.is_correct_answer(response)
        return math_problem, is_correct, agent_answer, real_answer

    def test_math_parallel(self, agent: callable, math_problems: list, max_workers: int = 8):
        problem_types = set([problem.type for problem in math_problems])
        results = {
            "score": 0, 
            "test_counts": {"Correct": 0, "Error": 0}, 
            "test_counts_by_type": {problem_type: {"Correct": 0, "Error": 0} for problem_type in problem_types},
            "erratic_problems": {problem_type: [] for problem_type in problem_types}
        }

        n_correct = 0
        n_completed = 0

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_task = {executor.submit(self.test_math_task, agent, math_problem): math_problem for math_problem in math_problems}

            for future in concurrent.futures.as_completed(future_to_task):
                task_number = future_to_task[future]
                math_problem, is_correct, agent_answer, real_answer = future.result()
                
                n_completed += 1
                print(f'Completed Tasks: {n_completed}/{len(math_problems)}. Correct: {is_correct}, Agent Answer: {agent_answer}, Real Answer: {real_answer}')
                print('\n-----------------------------------\n')

                if is_correct:
                    n_correct += 1
                    results["test_counts"]["Correct"] += 1
                    results["test_counts_by_type"][math_problem.type]["Correct"] += 1
                else:
                    results["erratic_problems"][math_problem.type].append(math_problem.problem_number)
                    results["test_counts"]["Error"] += 1
                    results["test_counts_by_type"][math_problem.type]["Error"] += 1

        results["score"] = round(n_correct/len(math_problems) * 100, 4)
        print(f'Correct: {n_correct}/{len(math_problems)}')
        print(results)

        return results
    
    def save_results(self, results: dict, save_path: str = None):
        # Save results to a json file
        if save_path:
            # Make sure path exists or create it
            if not os.path.exists(os.path.dirname(save_path)):
                os.makedirs(os.path.dirname(save_path))
            with open(save_path + "results.json", "w") as file:
                # Save beautified json
                json.dump(results, file, indent=4)


if __name__ == "__main__":
    mdl = MathDataLoader(data_dir=constants.MATH_DATASET_DIR)
    print("Loaded Math Data Loader with Problem Types: ", mdl.problem_types)   
    random_problem = mdl.get_random_problem()
    print("Random Problem: ", random_problem) 
    random_problems = mdl.get_random_problems(proportion=0.1)  # Get 10% of the problems
    print(f"Randomly selected {len(random_problems)} problems.")
    for level in [1, 2, 3, 4, 5]:
        random_problems = mdl.get_random_problems(proportion=0.1, level=level)  # Get 10% of the problems of level 2
        print(f"Randomly selected {len(random_problems)} problems of level 2.")