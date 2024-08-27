
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """


def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n_str = str(n)
    product = 1
    has_odd_digit = False
    
    for char in n_str:
        digit = int(char)
        if digit % 2 != 0:
            product *= digit
            has_odd_digit = True
    
    if not has_odd_digit:
        return 0
    
    return product

# Test cases to verify the correctness of the function
assert digits(1) == 1
assert digits(4) == 0
assert digits(235) == 15
assert digits(246) == 0
assert digits(13579) == 945
assert digits(222) == 0
assert digits(111) == 1  # Additional test case to ensure multiple single odd digits return the correct product
assert digits(102030) == 3  # Mixed even and odd digits
assert digits(0) == 0  # Edge case where n is 0

def check(candidate):

    # Check some simple cases
    assert candidate(5) == 5
    assert candidate(54) == 5
    assert candidate(120) ==1
    assert candidate(5014) == 5
    assert candidate(98765) == 315
    assert candidate(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert candidate(2468) == 0


check(digits)