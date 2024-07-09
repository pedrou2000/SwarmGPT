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
    "AgentAnwerReadyJudge": Judge_if_got_Answer,
    "AgentAnswerReadyJudgeSummarize": If_got_Answer_T_F,
    
}
