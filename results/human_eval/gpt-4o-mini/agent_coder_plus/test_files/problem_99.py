
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
    value_float = float(value)  # Convert the input string to a float

    # Check if the value is already an integer
    if value_float.is_integer():
        return int(value_float)
    
    # Get the floor and ceiling of the value
    floor_value = int(value_float // 1)  # Floor value
    ceil_value = floor_value + 1          # Ceiling value
    
    # Calculate the decimal part
    decimal_part = abs(value_float - floor_value)

    if decimal_part == 0.5:  # Check for the case of equidistant
        if value_float > 0:
            return ceil_value  # Round away from zero (up)
        else:
            return floor_value  # Round away from zero (down)
    else:
        return round(value_float)  # Regular rounding

# Example usage:
print(closest_integer("10"))      # Output: 10
print(closest_integer("15.3"))    # Output: 15
print(closest_integer("14.5"))    # Output: 15
print(closest_integer("-14.5"))   # Output: -15

def check(candidate):

    # Check some simple cases
    assert candidate("10") == 10, "Test 1"
    assert candidate("14.5") == 15, "Test 2"
    assert candidate("-15.5") == -16, "Test 3"
    assert candidate("15.3") == 15, "Test 3"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("0") == 0, "Test 0"


check(closest_integer)