#########################################################################
############################### Thinker #################################
#########################################################################

Analysis_conditions_objective = """
    Help me to analyze the conditions and the objective of a problem.
    You should only provide one objective.
    The conditions must be derived directly from the problem; deductions or calculations to establish these conditions are not allowed.
    You don't need to provide me with a solution for the time being.

    Example 1:
    Question:
    Louis earns a base monthly salary of $\\$$1,200 with 5$\\%$ commission on sales. For a month with $\\$$25,000 in sales, what are Louis's total earnings?
    Conditions:
    1. Louis earns a base monthly salary of $1,200.
    2. He also earns a commission of 5$\\%$ on sales.
    3. In a particular month, Louis makes $25,000 in sales.
    Objective:
    Calculate Louis's total earnings for the month, which includes both his base salary and the commission from the sales.

    Example 2:
    Question:
    A line segment has one endpoint at $(6,8)$ and midpoint at $(1,1)$. What is the sum of the coordinates of the other endpoint?
    Conditions:
    1. A line segment has one endpoint at (6,8).
    2. The midpoint of this line segment is at (1,1).
    Objective:
    1. Find the coordinates of the other endpoint of the line segment.
    2. Find the sum of these coordinates.

    Real question:
    Question:
    {Question}
"""

Fix_conditions_prompt = """
    I need you to fix a conclusion based on a problem. 
    You only need to find some content, which is similar to wrong the conclusion from the problem description as the fixed conclusion.
    You just need to provide the fixed conclusion, don't say any other words

    Example 1:
    problem:
    Avery earns 30$ each day, how much will he earn for 30 days?
    Wrong statement:
    Avery earns 20$ each day
    Fixed statement:
    Avery earns 30$ each day

    Example 2:
    problem:
    The sum of two numbers is 25 and their difference is 9. What is their product?
    Wrong statement:
    The sum of two numbers is 18
    Fixed statement:
    The sum of two numbers is 25

    Real question:
    problem:
    {question}
    Wrong statement:
    {Initial_conditions}
    Fixed statement:
"""

Discover_new_conditions = """
    I have some known conditions:
    {Known_conditions}
    And my objective is:
    {Objective}
    Please derive one most direct conditions with logical relationships based on the known conditions.
    NOTE:
    1. You are only allowed to use the known conditions to derive new conclusions.
    2. You have to use code to perform the math calculation.
"""

Summarize_Answer = """
    Please summarize your answer by using the following format:
    Based on Known condition ... , we can get: ... 
    Reason: ...
"""

Determine_Steps = """
    Help me to come up with one solution targeting at our objective. 

    Example 1:
    Known conditions: 
    1. f(3) = 5
    2. for all x > 0, f(3x) = f(x) + 2
    3. Because f(3x) = f(x) + 2, so f(9) = f(3) + 2
    4. Because f(3x) = f(x) + 2, and f(3) = 5, so f(9) = 7
    5. Because f(3x) = f(x) + 2, so f(27) = f(9) + 2
    Objective:
    find $f^{{-1}}(11)$
    Solutions:
    Step 1:
    Use f(9) to find f(27)
    Step 2:
    Use f(27) to find f(81)
    Step 3:
    Repeat until find x that f(x) = 11

    Example 2:
    Known conditions: 
    1. a + 1 / b = 22 / 7
    2. b + 1 / c = 8
    3. abc = 21
    4. c = 1 / (8 - b)
    5. a = (22 / 7) - (1 / b) 
    Objective:
    Calaculate c + 1 / a
    Solutions:
    Step 1:
    Substitude a in abc = 21 by (22 / 7) - (1 / b) 
    Step 2:
    Substitude c in abc = 21 by 1 / (8 - b) 
    Step 3:
    Calculate b 
    Step 4:
    Calculate a and c
    Step 5:
    Calculate c + 1 / a

    Real question:
    Known conditions:
    {Known_conditions}
    Objective:
    {Objective}
    Solutions:
"""

#########################################################################
################################# Judge #################################
#########################################################################

Judge_condtion = """
    I need you to determine if the statement is a condition included inside the problem.
    You are only allowed to use the 'True' or 'False' as the final answer.
    If it is correct, answer 'True'. 
    If it is not correct, answer 'False'. 

    Example 1:
    problem:
    Avery earns 30$ each day, how much will he earn for 30 days?
    Statement:
    Avery earns 20$ each day
    Judgement:
    False

    Example 2:
    problem:
    The sum of two numbers is 25 and their difference is 9. What is their product?
    Statement:
    The sum of two numbers is 25
    Judgement:
    True

    Real question:
    problem:
    {question}
    Statement:
    {Initial_conditions}
    Judgement:
"""

Judge_T_F = """
    I have some Known condtions:
    {Known_condtions}
    Help me to carefully verify if the statement:
    {condition_from_thinker} is correct.
    You have to use code to verify the math calculation.
"""

T_or_F_prompt = """
    Please just tell me if the statement is correct by using 'True' or 'False'.
"""

Judge_if_got_Answer = """
    I have some known conditions:
    {Known_condtions}
    And I want to {Objective}.
    Help me to determine if the objective can be obtained based on the known conditions or the objective is already one of the current conditions.
"""

If_got_Answer_T_F = """
    Please summarize your analysis just by using 'True' or 'False'.
"""



#########################################################################
############################## Executor #################################
#########################################################################

find_target = """
    I need you to find the final objective based on some steps.
    Our objective is:
    {Objective}
    We have:
    {Conditions}
    The steps that you should follow:
    {Steps}
    You answer:
"""

box_target = """
    Now you need to use \\boxed to mark your answer. Your final result should be converted to a float number.
    Please do not answer anything else, just give the float number marked with \\boxed.
"""