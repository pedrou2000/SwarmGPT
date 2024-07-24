

# Open txt file with prompt and read the prompt
with open("AgentCoder/prompts/test_designer_humaneval_prompt_update.txt", "r") as file:
    AgentTestGenerator_system = file.read()

with open("AgentCoder/prompts/humaneval_prompt_update.txt", "r") as file:
    AgentCoder_system = file.read()


AGENT_CODER = {
    "AgentTestGenerator": {
        "system": AgentTestGenerator_system,
        "user": """
## Prompt :\n{method_description}\n ## Completion:\n
        """,
    },
    "AgentCoder": {
        "system": AgentCoder_system,
        "user": """
## Prompt :\n{method_description}\n ## Completion:\n
        """,
    },
    "AgentTestExecutor": {
        "system": """
Your task is to run the code provided (without any changes)together with the tests and report whether the code passes the tests or not. 
It is very important that you do not modify the code, just run it and provide feedback.
        """,
        "user": """
## Code to test (Do not modify): \n{completed_method}\n {test_cases}\n\n ## Feedback: \n
        """,
        "parser_system": """
Given the code which has been run and the feedback provided, please parse the feedback into a structured format.
You should return a boolean value indicating whether the tests passed or not and a string with the feedback.
        """
    },
    "AgentCodeRefiner": {
        "system": """
You are an expert coder. Another coder has written a method that is not correct, as it does not pass the tests. 
The tests have been run by another agent, which has provided feedback on how to make the code pass the tests.
Your task is to refine the code so that it passes the tests.
        """,
        "user": """
## Code to Refine: \n{completed_method}\n\n ## Feedback on the code after running the tests: \n {feedback}\n\n ## Improved Code: \n
        """,
    }
}