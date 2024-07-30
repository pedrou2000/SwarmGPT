import os, sys
sys.path.append(os.path.abspath(__file__))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from langchain_core.pydantic_v1 import BaseModel, Field
import operator 
from typing import Annotated, List, Optional

import constants

class AgentCoderPlusState():
    incomplete_method: Annotated[str, Field(description="Incomplete method to be completed")]
    generated_tests: Annotated[str, Field(description="Generated tests for the method")]
    completed_method: Annotated[str, Field(description="Completed method")]
    tests_passed: Annotated[bool, Field(description="Whether the tests passed or not in the generated code")]
    feedback: Annotated[str, Field(description="Feedback from the tests run on the generated code")]
    current_iterations: Annotated[int, Field(description="Current number of iterations in the refinement looop")]
    max_iterations: Annotated[int, Field(description="Maximum number of iterations in the refinement loop")]
    passed_tests_threshold: Annotated[float, Field(description="Threshold for the proportion of tests that need to pass")]
    refine_else_restart: Annotated[bool, Field(description="Whether to refine the method, restart or continue")]

    def __init__(
            self, 
            incomplete_method: str = None, 
            generated_tests: str = None, 
            completed_method: str = None, 
            tests_passed: bool = False,
            feedback: str = None,
            current_iterations: int = -1,
            max_iterations: int = -1,
            passed_tests_threshold: float = -1, 
            refine_else_restart: bool = None,
        ):
        if incomplete_method is not None:
            self.incomplete_method = incomplete_method
        if generated_tests is not None:
            self.generated_tests = generated_tests
        if completed_method is not None:
            self.completed_method = completed_method
        if tests_passed is not None:
            self.tests_passed = tests_passed
        if feedback is not None:
            self.feedback = feedback
        if current_iterations != -1:
            self.current_iterations = current_iterations
        if max_iterations != -1:
            self.max_iterations = max_iterations
        if passed_tests_threshold != -1:
            self.passed_tests_threshold = passed_tests_threshold
    
    def __str__(self) -> str:
        return f"AgentCoder State with incomplete method: {self.incomplete_method}"

if __name__ == "__main__":
    macm_state = AgentCoderState(incomplete_method='def some_method():\n')
    print(macm_state)
