
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


def apply_operations(operators, operands):
    if len(operators) != len(operands) - 1:
        raise ValueError("Invalid input lengths.")
    
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '**': 3}
    output = []
    ops_stack = []
    
    # Convert to postfix notation (RPN)
    for i in range(len(operands)):
        output.append(operands[i])
        if i < len(operators):
            while ops_stack and precedence[ops_stack[-1]] >= precedence[operators[i]]:
                output.append(ops_stack.pop())
            ops_stack.append(operators[i])
    
    while ops_stack:
        output.append(ops_stack.pop())
    
    # Evaluate the RPN expression
    stack = []
    for token in output:
        if isinstance(token, (int, float)):
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
            elif token == '//':
                stack.append(a // b)
            elif token == '**':
                stack.append(a ** b)
    
    return stack[0]

# Example test cases
print(apply_operations(['+', '*', '-'], [2, 3, 4, 5]))  # Expected Result: 9
print(apply_operations(['*', '+', '-'], [2, 3, 4, 5]))  # Expected Result: 5
print(apply_operations(['-', '**'], [5, 2, 3]))         # Expected Result: 2
print(apply_operations(['**', '//'], [2, 3, 8]))        # Expected Result: 0
print(apply_operations(['+', '-'], [9, 4, 2]))          # Expected Result: 11
print(apply_operations(['*'], [3, 4]))                  # Expected Result: 12
print(apply_operations(['//'], [8, 2]))                 # Expected Result: 4
print(apply_operations(['+'], [0, 0]))                  # Expected Result: 0
print(apply_operations(['-'], [10, 5]))                 # Expected Result: 5
print(apply_operations(['**', '*', '+'], [2, 3, 2, 1])) # Expected Result: 37

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)