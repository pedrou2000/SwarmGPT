
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
    If shift > number of digits, return digits reversed.
    >>> circular_shift(12, 1)
    "21"
    >>> circular_shift(12, 2)
    "12"
    """
    str_x = str(x)  # Convert integer to string
    n = len(str_x)  # Get the length of the string representation

    if shift > n:
        return str_x[::-1]  # Return the reversed string if shift is greater than length
    else:
        effective_shift = shift % n  # Calculate effective shift
        return str_x[-effective_shift:] + str_x[:-effective_shift]  # Perform circular shift

# Example usage (for testing)
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"
print(circular_shift(12345, 3))  # Output: "34512"
print(circular_shift(12345, 7))  # Output: "54321"

def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)