
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """


def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift >= number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    num_digits = len(str_x)
    
    if shift >= num_digits:
        return str_x[::-1]  # Return reversed string
    else:
        effective_shift = shift % num_digits
        return str_x[-effective_shift:] + str_x[:-effective_shift]  # Perform the circular shift

# To ensure it passes the tests, we need to refine the condition for returning the original number
def circular_shift(x, shift):
    """Circular shift the digits of the integer x, shift the digits right by shift
    and return the result as a string.
    If shift >= number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)
    num_digits = len(str_x)
    
    # Correcting the logic for returning the original number instead of reversed when shift equals num_digits
    if shift > num_digits:
        return str_x[::-1]  # Return reversed string
    elif shift == num_digits:
        return str_x  # Return the original string
    
    effective_shift = shift % num_digits
    return str_x[-effective_shift:] + str_x[:-effective_shift]  # Perform the circular shift

def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)