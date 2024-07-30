
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
    # Convert x to a string to manipulate digits
    x_str = str(x)
    n = len(x_str)
    
    # Calculate the effective shift
    effective_shift = shift % n
    
    # If shift is 0, return the original string
    if effective_shift == 0:
        return x_str
    
    # If shift is greater than or equal to the number of digits, return the reversed string
    if shift > n:
        return x_str[::-1]
    
    # Perform the circular shift
    shifted_str = x_str[-effective_shift:] + x_str[:-effective_shift]
    
    return shifted_str

# Example usages
print(circular_shift(12, 1))  # Output: "21"
print(circular_shift(12, 2))  # Output: "12"

def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)