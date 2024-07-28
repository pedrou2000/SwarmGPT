
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
    # Convert the string to a float
    num = float(value)
    
    # Check if the number is exactly halfway between two integers
    if num > 0:
        if num % 1 == 0.5:
            return int(num) + 1  # Round up for positive numbers
        else:
            return round(num)
    else:  # num is negative
        if num % 1 == -0.5:
            return int(num) - 1  # Round down for negative numbers
        else:
            return round(num)

# Testing the function with the provided examples
print(closest_integer("10"))    # Output: 10
print(closest_integer("15.3"))  # Output: 15
print(closest_integer("14.5"))  # Output: 15
print(closest_integer("-14.5")) # Output: -15

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)