import re, os, json
import runpy
from datasets import load_dataset

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