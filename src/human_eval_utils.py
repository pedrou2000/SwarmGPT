import concurrent.futures
import re, os, json
import runpy
from datasets import load_dataset
import constants

def load_human_eval():
    return load_dataset("openai_humaneval", split="test")

def parse_python_code(code: str) -> str:
    """
    Check if the input string contains a ```python``` code block and return it. 
    Else return None.

    Example: 
    ```python
    even_digits = [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0]
    return sorted(even_digits)
    ```
    """
    # Regular expression to match the ```python code block
    pattern = r'```python(.*?)```'
    
    # Search for the pattern in the input string
    match = re.search(pattern, code, re.DOTALL)
    
    # If a match is found, return the code block; else return None
    if match:
        return match.group(1)
    else:
        return None

def construct_test_program(prompt: str, completion: str, test_program: str, mehod_name: str, save_path: str = None) -> str:
    test_program = f"{prompt}\n{completion}\n{test_program}\ncheck({mehod_name})"
    if save_path:
        # Make sure path exists or create it
        save_path = os.path.abspath(save_path)
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
        with open(save_path, "w") as file:
            file.write(test_program)
    return test_program

def code_runs_without_errors(code: str = None, file_path: str = None) -> bool:
    # Run the code in the file with the exec function and check if it raises any exceptions
    try:
        # code_obj = compile(code, '<string>', 'exec')
        # exec(code_obj)
        if code and not file_path:
            with open("test.py", "w") as file:
                file.write(code)
            runpy.run_path("test.py")
        elif file_path and not code:
            runpy.run_path(file_path)
        else:
            print("Either code or file_path should be provided.")
            return (False, "IncorrectInput")
    except AssertionError as ae:
        print(f"AssertionError in check_code_execution: {ae}")
        return (False, "AssertionError")
    except Exception as e:
        print(f"Error in check_code_execution: {e}")
        return (False, "Error")

    return (True, "NoError")

def save_results(results: dict, save_path: str = None):
    # Save results to a json file
    if save_path:
        # Make sure path exists or create it
        if not os.path.exists(os.path.dirname(save_path)):
            os.makedirs(os.path.dirname(save_path))
        with open(save_path + "results.json", "w") as file:
            # Save beautified json
            json.dump(results, file, indent=4)


def get_erratic_problems(file_path):
    # Load the JSON data from the file
    with open(file_path + 'results.json', 'r') as file:
        data = json.load(file)
    
    # Return the list of erratic problems
    return data.get("erratic_problems", [])

def test_humaneval_task(agent: callable, task_number: int, task: dict, max_iterations: int, passed_tests_threshold: float):

    completion = agent(task['prompt'], max_iterations=max_iterations, passed_tests_threshold=passed_tests_threshold)

    test_path = constants.HUMAN_EVAL_AGENT_CODER_DIR + 'test_files/' + f'problem_{task_number}.py'
    test_program = construct_test_program(task['prompt'], completion, task['test'], task['entry_point'], save_path=test_path)
    (code_works, reason) = code_runs_without_errors(file_path=test_path)
    
    return task_number, code_works, reason

def test_humaneval_parallel(agent: callable, task_numbers: list, tasks: list, max_iterations: int, passed_tests_threshold: float):
    results = {
        "score": 0, 
        "test_counts": {"NoError": 0, "Error": 0, "AssertionError": 0, "IncorrectInput": 0}, 
        "erratic_problems": [],
        "tests_results": {}
    }

    n_correct = 0

    with concurrent.futures.ThreadPoolExecutor() as executor:
        future_to_task = {executor.submit(test_humaneval_task, agent, task_number, tasks[task_number], max_iterations, passed_tests_threshold): task_number for task_number in task_numbers}

        for future in concurrent.futures.as_completed(future_to_task):
            task_number = future_to_task[future]
            task_number, code_works, reason = future.result()
            
            print(f'Problem {task_number} - Tests Passed: {code_works}' + f' - Reason: {reason if not code_works else ""}')
            print('\n-----------------------------------\n')

            if code_works:
                n_correct += 1
            else:
                results["erratic_problems"].append(task_number)
            if reason in results["test_counts"]:
                results["test_counts"][reason] += 1
            else:
                results["test_counts"][reason] = 1
            results["tests_results"][task_number] = (code_works, reason)

    results["score"] = round(n_correct/len(task_numbers) * 100, 4)
    print(f'Correct: {n_correct}/{len(task_numbers)}')
    print(results)

    return results



if __name__ == "__main__":
    code = """
    adsfsdfas
    ```python
    even_digits = [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0]
    return sorted(even_digits)
    ```
    asdfasfasfasd
    ```python
    even_digits = [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0]
    return sorted(even_digits)
    ```
    """
    parsed_code = parse_python_code(code)
    print(parsed_code) # Output: even_digits = [i for i in range(min(a, b), max(a, b) + 1) if i % 2 == 0]