
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
    # Convert number to absolute value to handle negative numbers
    num = abs(num)
    
    # Convert number to string to iterate over each digit
    num_str = str(num)
    
    # Initialize counters
    even_count = 0
    odd_count = 0
    
    # Iterate over each digit in the string representation of the number
    for digit in num_str:
        # Convert digit back to integer
        digit = int(digit)
        
        # Check if the digit is even or odd
        if digit % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Return the counts as a tuple
    return (even_count, odd_count)

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