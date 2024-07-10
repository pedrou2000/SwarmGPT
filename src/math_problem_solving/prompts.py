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
