
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """


from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """ Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    # Determine lower and upper bounds
    lower, upper = min(a, b), max(a, b)
    
    # List to hold even numbers
    even_numbers = []
    
    # Iterate over the range from lower to upper
    for number in range(lower, upper + 1):
        if number % 2 == 0:  # Check if the number is even
            even_numbers.append(number)
    
    return even_numbers

def check(candidate):

    # Check some simple cases
    assert candidate(2, 10) == [2, 4, 6, 8], "Test 1"
    assert candidate(10, 2) == [2, 4, 6, 8], "Test 2"
    assert candidate(132, 2) == [2, 4, 6, 8], "Test 3"
    assert candidate(17,89) == [], "Test 4"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(generate_integers)