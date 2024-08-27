
def generate_integers(a, b):
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    generate_integers(2, 8) => [2, 4, 6, 8]
    generate_integers(8, 2) => [2, 4, 6, 8]
    generate_integers(10, 14) => []
    """


def generate_integers(a, b):
    """ Given two positive integers a and b, return the even digits between a
    and b, in ascending order.
    
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """
    # Determine the minimum and maximum between a and b
    min_value = min(a, b)
    max_value = max(a, b)
    
    result = []
    
    # Iterate from min_value to max_value
    for num in range(min_value, max_value + 1):
        # Check if the number is even
        if num % 2 == 0:
            result.append(num)
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(2, 10) == [2, 4, 6, 8], "Test 1"
    assert candidate(10, 2) == [2, 4, 6, 8], "Test 2"
    assert candidate(132, 2) == [2, 4, 6, 8], "Test 3"
    assert candidate(17,89) == [], "Test 4"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(generate_integers)