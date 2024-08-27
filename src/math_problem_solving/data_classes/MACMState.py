import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from langchain_core.pydantic_v1 import BaseModel, Field
import operator 
from typing import Annotated, List, Optional

from data_classes.MathDataLoader import MathDataLoader
from data_classes.MathProblem import MathProblem
import constants

class MACMState():
    math_problem: Annotated[MathProblem, Field(description="Math problem to solve")]  
    max_iterations: Annotated[int, Field(description="Maximum number of thinker-judge iterations")]
    current_iterations: Annotated[int, Field(description="Current number of thinker-judge iterations")]
    verified_conditions: Annotated[List[str], Field(description="List of verified conditions")]
    unverified_conditions: Annotated[List[str], Field(description="List of unverified conditions")]
    objectives: Annotated[List[str], Field(description="List of objectives to solve the problem")]
    steps: Annotated[List[str], Field(description="List of steps to be executed by the executor to solve the problem")]
    final_answer: Annotated[str, Field(description="Final answer to the math problem")]

    # Meta State
    final_answers: Annotated[dict, Field(description="Final answers to the math problems")]
    n_multi_agent_iterations: Annotated[int, Field(description="Number of MACM iterations run")]
    n_single_agent_iterations: Annotated[int, Field(description="Number of single agent iterations run")]
    current_meta_iterations: Annotated[int, Field(description="Current MACM iteration number")]
    multi_agent_completed: Annotated[bool, Field(description="Flag to indicate if the MACM part of the algorithm has been completed")]

    # Test Generation
    generated_tests: Annotated[str, Field(description="Generated tests for the math problem")] 
    feedback: Annotated[str, Field(description="Feedback on how to fix the tests")]
    passed_tests_threshold: Annotated[float, Field(description="Threshold for passing the tests of the tests")]
    tests_passed: Annotated[bool, Field(description="Flag to indicate if the tests are considered correct")]

    def __init__(
            self, 
            math_problem: MathProblem = None,
            max_iterations: Optional[int] = None,
            current_iterations: Optional[int] = None,   
            verified_conditions: Optional[List[str]] = None, 
            unverified_conditions: Optional[List[str]] = None,
            objectives: Optional[List[str]] = None,
            steps: Optional[List[str]] = None,
            final_answer: Optional[str] = None,
            final_answers: Optional[dict] = None,
            n_multi_agent_iterations: Optional[int] = None,
            n_single_agent_iterations: Optional[int] = None,
            current_meta_iterations: Optional[int] = None, 
            multi_agent_completed: Optional[bool] = False,
            generated_tests: Optional[str] = None,
            feedback: Optional[str] = None, 
            passed_tests_threshold: Optional[float] = None,
            tests_passed: Optional[bool] = None,
        ):
        if math_problem is not None:
            self.math_problem = math_problem
        if max_iterations is not None:
            self.max_iterations = max_iterations
        if current_iterations is not None:
            self.current_iterations = current_iterations
        if verified_conditions is not None:
            self.verified_conditions = verified_conditions
        if unverified_conditions is not None:
            self.unverified_conditions = unverified_conditions
        if objectives is not None:
            self.objectives = objectives
        if steps is not None:
            self.steps = steps
        if final_answer is not None:
            self.final_answer = final_answer
        if final_answers is not None:
            self.final_answers = final_answers
        if n_multi_agent_iterations is not None:
            self.n_multi_agent_iterations = n_multi_agent_iterations
        if n_single_agent_iterations is not None:
            self.n_single_agent_iterations = n_single_agent_iterations
        if current_meta_iterations is not None:
            self.current_meta_iterations = current_meta_iterations
        if multi_agent_completed is not None:
            self.multi_agent_completed = multi_agent_completed
        if generated_tests is not None:
            self.generated_tests = generated_tests
        if feedback is not None:
            self.feedback = feedback
        if passed_tests_threshold is not None:
            self.passed_tests_threshold = passed_tests_threshold
        if tests_passed is not None:
            self.tests_passed = tests_passed
    
    def __str__(self) -> str:
        return f"MACM State with math problem: {self.math_problem}"

if __name__ == "__main__":
    data_loader = MathDataLoader(data_dir=constants.MATH_DATASET_DIR)
    math_problem = data_loader.get_random_problem()
    macm_state = MACMState(math_problem=math_problem, max_iterations=1)
    print(macm_state)
