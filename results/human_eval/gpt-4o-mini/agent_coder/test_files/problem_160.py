
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


from typing import List

def do_algebra(operator: List[str], operand: List[int]) -> int:
    """ 
    Evaluates the algebraic expression defined by the operators and operands.
    """
    # Convert operands and operators into a list of tokens
    result_stack = []
    current_result = operand[0]
    
    for i in range(len(operator)):
        op = operator[i]
        next_operand = operand[i + 1]

        if op in ('*', '//', '**'):
            if op == '*':
                current_result *= next_operand
            elif op == '//':
                current_result //= next_operand
            elif op == '**':
                current_result **= next_operand
        else:
            # Add current result to stack and reset it
            result_stack.append(current_result)
            result_stack.append(op)  # Push the operator
            current_result = next_operand  # Reset current result to the next operand

    # Push the last result to the stack
    result_stack.append(current_result)

    # Now evaluate the stack, processing + and -
    final_result = result_stack[0]
    i = 1
    while i < len(result_stack):
        op = result_stack[i]
        next_value = result_stack[i + 1]
        if op == '+':
            final_result += next_value
        elif op == '-':
            final_result -= next_value
        i += 2  # Move to the next operator

    return final_result

# Example usage:
print(do_algebra(['+', '*', '-'], [2, 3, 4, 5]))  # Should return 9

def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(do_algebra)