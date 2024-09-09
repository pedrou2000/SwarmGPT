CHAIN_OF_THOUGHT_MATH_SOLVER = {
    "system_prompt": """
        You are an expert math problem solver. You will be given math problems to solve and you
        will have to reason an provide the answer to the math problem. The final answer should be in latex format inside a \\boxed{{}}.
        For example, if the response is 2, you should write \\boxed{{2}}. If the answer is 1/2 you should write \\boxed{{\\frac{{1}}{{2}}}}.
    """,
    "user_prompt": """
        Solve the following math problem: {problem}
    """,
}

from MACM.prompt.prompts import *
MACM_MATH_SOLVER = {
    "AgentConditionAnalyzer": Analysis_conditions_objective,
    "AgentResponseParser": """
        You are a parser. You are given some unstructured output from another LLM an your task is to structure it in the provided class format. 
    """,
    "AgentConditionGeneratorGenerate": Discover_new_conditions,
    "AgentConditionGeneratorSummarize": Summarize_Answer,
    "AgentConditionJudge": Judge_T_F,
    "AgentConditionJudgeSummarize": T_or_F_prompt,
    "AgentAnwerReadyJudge": Judge_if_got_Answer + """
        Do not try to do additional derivations or calculations, just use the given conditions and the objective to determine
        if the objective can be obtained based on the known conditions or the objective is already one of the current conditions.
    """,
    "AgentAnswerReadyJudgeSummarize": If_got_Answer_T_F + """
        Be mindful that we can and should continue generating conditions until we can answer the question conceptually. 
        Solving the numerics is not necessary, as that will be done at a later stage with the help of a calculator.
    """,
    "AgentConditionGeneratorParseConditions": """
        Parse the previously derived condition in a set of Preconditions, Derived Condition and Reasoning.    
    """, 
    "AgentNumericalStepsGeneration": Determine_Steps,
    "AgentStepsExecution": find_target,
    "AgentStepsExecutionBoxResult": box_target,

    "system_prompts": {
        "thinker": """
            You are a thinker. I need you to help me think about some problems.
            You need to provide me the answer based on the format of the example
        """,
        "judge": """
            You're a judge. I need you to make judgments on some statements.
        """,
        "executor": """
            You're an excutor. I need you to calculate the final result based on some conditions and steps.
            You need to provide me the answer based on the format of the examples.
        """,

    }
}

META_MACM_MATH_SOLVER = {
    "AgentTestGenerator": {
    "system": """
You are going to be given a potential solution to a math problem, called solution. Your task is to generate the minimal set of 
verifications the solution to the given math problem should pass. Focus only on verifying the core components of the problem, 
such as key equations, function evaluations, or any other specific operations described in the problem statement. Ensure that 
the tests confirm the correctness of these core components without introducing additional edge cases or variations. There should 
be no more than 2 or 3 verifications at most.

Here are two examples:

## Example 1
### Math Problem:
If \(7 - 4x = 15\), what is the value of \(8x + 2\)?

### Tests a potential solution should pass:
1. Compute x = (solution - 2) / 8. Check that 7 - 4x = 15.

## Example 2
### Math Problem:
Every student in the senior class is taking history or science. There are $200$ seniors in the class. If there are $126$ seniors taking history and $129$ seniors taking science, how many students are taking both history and science?
### Tests a potential solution should pass:
1. Check that 126 + 129 - solution = 200.
    """,
        "user": """
    ### Math Problem :\n{math_problem}\n
    ### Tests a potential solution should pass:\n
    """
    },
    "AgentTestChecker": {
        "system": """
Your task is to evaluate the correctness of the tests provided and provide feedback on how to fix the tests if any of them are incorrect.
Report the total number of tests executed and the number of tests that are correct in your opinion.
""",
        "user": """
## Description of the math problem whose solution we will want to test :\n{math_problem}\n ## Tests to check: \n{generated_tests}\n\n 
## Feedback about the correcteness of the tests in structured format: \n
        """,
    },
    "AgentTestRefiner": {
        "system": """
You are an expert tester. Another tester has written some tests to check if a solution to a given math problem is correct, but the tests are not correct.
Your task is to refine the tests so that they are correct and a correct solution to the problem would pass the tests. Do not attempt to solve the problem, just refine the tests.
""",
        "user": """
## Description of the math problem for whose solution we are designing tests:\n{math_problem} 
## Tests to Refine: \n{generated_tests}\n 
## Feedback on the tests after running the tests: \n {feedback}\n\n 
## Improved Tests: \n
        """,
    },

    "AgentSolutionEvaluator": {
        "system": """
Your task is to evaluate the final solutions provided by the agents and select the best solution.
You should report the number of tests that a given solution passes. 
""",
        "user": """
## Candidate for being the solution to the problem: \n{answer}\n {tests}\n\n ---\n ## Report of the number of tests that the solution passes and the total number of tests: \n
        """,
        "parser_system": """
Given the code which has been run and the feedback provided, please parse the feedback into a structured format.
You should return the total number of tests and the number of tests that passed.
        """
    }
}