
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """


def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    # Handle negative numbers by taking the absolute value of the number
    num = abs(num)
    
    # Convert number to string to iterate over each digit
    num_str = str(num)
    
    # Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Iterate through each digit in the string representation
    for digit in num_str:
        digit_int = int(digit)
        if digit_int % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Return the result as a tuple
    return (even_count, odd_count)

# Example usage:
# print(even_odd_count(-12))   # Output: (1, 1)
# print(even_odd_count(123))   # Output: (1, 2)

def check(candidate):

    # Check some simple cases
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)
    assert candidate(-2) == (1, 0)
    assert candidate(-45347) == (2, 3)
    assert candidate(0) == (1, 0)


    # Check some edge cases that are easy to work out by hand.
    assert True


check(even_odd_count)