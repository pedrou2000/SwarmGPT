

# Open txt file with prompt and read the prompt
with open("../agent_coder/AgentCoder/prompts/test_designer_humaneval_prompt_update.txt", "r") as file:
    AgentTestGenerator_system = file.read()

with open("../agent_coder/AgentCoder/prompts/humaneval_prompt_update.txt", "r") as file:
    AgentCoder_system = file.read()


AGENT_CODER_PLUS = {
    "AgentTestGenerator": {
        "system": AgentTestGenerator_system,
        "user": """
## Prompt :\n{method_description}\n ## Completion:\n
        """,
    },
    "AgentTestChecker": {
        "system": """
Your task is to evaluate the correctness of the tests provided and provide feedback on how to fix the tests if any of them are incorrect.
Also determine if the tests should be refined or start from scratch.
""",
        "user": """
## Description of the method to test :\n{method_description}\n ## Tests to check: \n{generated_tests}\n\n ## Feedback in structured format: \n
        """,
    },
    "AgentTestRefiner": {
        "system": """
You are an expert tester. Another tester has written some tests that are not correct.
Your task is to refine the tests so that they are correct.
""",
        "user": """
## Description of the method to test :\n{method_description} ## Tests to Refine: \n{generated_tests}\n ## Feedback on the tests after running the tests: \n {feedback}\n\n ## Improved Tests: \n
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
Your task is to run the code provided (without any changes) together with the tests and report whether the code passes the tests or not. 
It is very important that you do not modify the code, just run it and provide feedback.
        """,
        "user": """
## Code to test (Do not modify): \n{completed_method}\n {test_cases}\n\n ## Feedback: \n
        """,
        "parser_system": """
Given the code which has been run and the feedback provided, please parse the feedback into a structured format.
You should return the total number of tests, the number of tests that passed, and the feedback provided.
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