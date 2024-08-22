
def closest_integer(value):
    '''
    Create a function that takes a value (string) representing a number
    and returns the closest integer to it. If the number is equidistant
    from two integers, round it away from zero.

    Examples
    >>> closest_integer("10")
    10
    >>> closest_integer("15.3")
    15

    Note:
    Rounding away from zero means that if the given number is equidistant
    from two integers, the one you should return is the one that is the
    farthest from zero. For example closest_integer("14.5") should
    return 15 and closest_integer("-14.5") should return -15.
    '''


def closest_integer(value):
    import math
    
    # Convert the input string to a float
    num = float(value)
    
    # Determine the closest integer
    if num > 0:
        if num - math.floor(num) < 0.5:
            return math.floor(num)
        else:
            return math.ceil(num)
    elif num < 0:
        if num - math.ceil(num) > -0.5:
            return math.ceil(num)
        else:
            return math.floor(num)
    else:
        return 0  # If the value is exactly 0, return 0

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)