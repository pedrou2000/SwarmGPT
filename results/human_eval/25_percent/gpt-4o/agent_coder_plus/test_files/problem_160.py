
def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebric 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.

    """


def do_algebra(operator, operand):
    """
    Given two lists operator, and operand. The first list has basic algebra operations, and 
    the second list is a list of integers. Use the two given lists to build the algebraic 
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + ) 
    Subtraction ( - ) 
    Multiplication ( * ) 
    Floor division ( // ) 
    Exponentiation ( ** ) 

    Example:
    operator['+', '*', '-']
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
    """
    from operator import add, sub, mul, floordiv, pow
    
    # Mapping operators to their corresponding functions
    op_func = {
        '+': add,
        '-': sub,
        '*': mul,
        '//': floordiv,
        '**': pow
    }
    
    # Operator precedence
    precedence = {
        '**': 3,
        '*': 2,
        '//': 2,
        '+': 1,
        '-': 1
    }
    
    # Initialize stacks for operands and operators
    operand_stack = []
    operator_stack = []
    
    # Helper function to apply an operator to the top two operands in the stack
    def apply_operator():
        right = operand_stack.pop()
        left = operand_stack.pop()
        oper = operator_stack.pop()
        operand_stack.append(op_func[oper](left, right))
    
    # Add the first operand to the stack
    operand_stack.append(operand[0])
    
    # Process each operator and operand pair
    for i in range(len(operator)):
        while (operator_stack and 
               precedence[operator_stack[-1]] >= precedence[operator[i]]):
            apply_operator()
        operator_stack.append(operator[i])
        operand_stack.append(operand[i + 1])
    
    # Apply remaining operators
    while operator_stack:
        apply_operator()
    
    return operand_stack[0]

# Example usage:
operator = ['+', '*', '-']
operand = [2, 3, 4, 5]
print(do_algebra(operator, operand))  # Output should be 9

# Running additional test cases to verify the fix
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Expected: 9
print(do_algebra(['+', '+'], [1, 2, 3]))  # Expected: 6
print(do_algebra(['-', '*', '//'], [10, 3, 2, 2]))  # Expected: 11
print(do_algebra(['**', '+'], [2, 3, 2]))  # Expected: 11
print(do_algebra(['-', '//'], [8, 6, 2]))  # Expected: 5
print(do_algebra(['*', '*', '*'], [1, 2, 3, 4]))  # Expected: 24
print(do_algebra(['+', '-', '+'], [10, 2, 3, 4]))  # Expected: 9
print(do_algebra(['**', '-', '+'], [2, 3, 4, 5]))  # Expected: -3
print(do_algebra(['+', '*', '+', '*'], [1, 2, 3, 4, 5]))  # Expected: 27
print(do_algebra(['//', '+', '*'], [9, 3, 2, 4]))  # Expected: 16

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)