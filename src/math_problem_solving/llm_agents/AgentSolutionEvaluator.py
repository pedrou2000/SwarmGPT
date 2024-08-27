import sys, os
sys.path.append(os.getcwd())
sys.path.append(os.path.dirname(os.getcwd()))
sys.path.append(os.path.dirname(os.path.dirname(os.getcwd())))

from generic_agents.CodeInterpreterAgent import CodeInterpreterAgent
import prompts

from langchain_core.pydantic_v1 import BaseModel
from typing import Any, List
import operator

class SolutionEvaluatorOutput(BaseModel):
    n_passed_tests: int
    n_total_tests: int

class AgentSolutionEvaluator(CodeInterpreterAgent):
    system_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentSolutionEvaluator"]["system"]
    test_executor_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentSolutionEvaluator"]["user"]
    parser_system_prompt: str = prompts.META_MACM_MATH_SOLVER["AgentSolutionEvaluator"]["parser_system"]

    def __init__(self):
        # Pass the system_prompt specific to AgentTestExecutor to the base class
        super().__init__(system_prompt=self.system_prompt)
        
    def __call__(self, state) -> Any:
        print("In AgentSolutionEvaluator")

        # print(f"Generated Tests: \n{state.generated_tests}")

        proportion_tests_passed_dict = {}

        for answer in state.final_answers:
            prompt_args = {
                "answer": answer,
                "tests": state.generated_tests
            }
            agent_response = self.user_prompt(self.test_executor_prompt, prompt_args)
            self.delete_all_messages()

            input_to_parse = answer + state.generated_tests + agent_response
            output = self.structured_output(response_class=SolutionEvaluatorOutput, system_prompt=self.parser_system_prompt, message=input_to_parse)

            proportion_tests_passed = output.n_passed_tests / output.n_total_tests

            proportion_tests_passed_dict[answer] = proportion_tests_passed
        
        # Select the best answer based on the proportion of tests passed and the frequency of the answer in state.final_answers
        max_value = max(proportion_tests_passed_dict.values())
        answers_with_max_value = [answer for answer, proportion in proportion_tests_passed_dict.items() if proportion == max_value]
        # If there's more than one answer with the maximum proportion, select based on frequency in state.final_answers
        if len(answers_with_max_value) > 1:
            # Find the answer among those with the max proportion that has the highest count in state.final_answers
            state.final_answer = max(answers_with_max_value, key=lambda answer: state.final_answers.get(answer, 0))
        else:
            # If only one answer has the maximum proportion, choose it
            state.final_answer = answers_with_max_value[0]


        print(f'\n'  + '-'*20)
        for key, value in proportion_tests_passed_dict.items():
            print(f"Proportion tests passed: {value} and frequency: {state.final_answers[key]} for solution: \n{key}\n")
        print(f'\n'  + '-'*20)

        self.delete_all_messages()
        return state


class State(BaseModel):
    final_answer: str = None
    final_answers: dict = None
    generated_tests: str = None

if __name__ == "__main__":  
    # Unit tests to check that a function sum is correctly implemented
    tests = """
        assert summ([1, 2, 3]) == 6
        assert summ([1, 2, 3, 4]) == 10
        assert summ([1, 2, 3, 4, 5]) == 15
    """

    # The final answers have as key programs that aim to implement the sum function
    final_answers = {
        """
def summ(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum
        """: 2,
        """
def summ(arr):
    return sum(arr)
        """: 1,
        """
def summ(arr):
    sum = 10
    return sum
        """: 3
    }

    tests = """
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,5,2,3,4]) == [1, 2, 4, 3, 5]
    assert candidate([-2,-3,-4,-5,-6]) == [-4, -2, -6, -5, -3]
    assert candidate([1,0,2,3,4]) == [0, 1, 2, 4, 3]
    assert candidate([]) == []
    assert candidate([2,5,77,4,5,3,5,7,2,3,4]) == [2, 2, 4, 4, 3, 3, 5, 5, 5, 7, 77]
    assert candidate([3,6,44,12,32,5]) == [32, 3, 5, 6, 12, 44]
    assert candidate([2,4,8,16,32]) == [2, 4, 8, 16, 32]
    assert candidate([2,4,8,16,32]) == [2, 4, 8, 16, 32]
"""

    final_answers = {"""
[Code]
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))

# Example usage:
print(sort_array([1, 5, 2, 3, 4]))  # Output: [1, 2, 3, 4, 5]
print(sort_array([-2, -3, -4, -5, -6]))  # Output: [-6, -5, -4, -3, -2]
print(sort_array([1, 0, 2, 3, 4]))  # Output: [0, 1, 2, 3, 4]
[/Code]
""": 1,
    """
def sort_array(arr):
    return sorted(arr, key=lambda x: (bin(x).count('1'), x))
""": 2,
}
    
    state = State(final_answers=final_answers, generated_tests=tests)
    final_answer = AgentSolutionEvaluator()(state).final_answer
    print(final_answer)