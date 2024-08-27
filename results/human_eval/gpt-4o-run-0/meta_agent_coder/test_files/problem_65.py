
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
    digits = str(x)
    num_digits = len(digits)
    effective_shift = shift % num_digits

    if effective_shift == 0:
        return digits
    elif shift > num_digits:
        return digits[::-1]
    else:
        return digits[-effective_shift:] + digits[:-effective_shift]

# Example usage
print(circular_shift(12, 1))  # Should output "21"
print(circular_shift(12, 2))  # Should output "12"
print(circular_shift(12345, 3))  # Should output "34512"
print(circular_shift(12345, 10))  # Should output "54321"

def check(candidate):

    # Check some simple cases
    assert candidate(100, 2) == "001"
    assert candidate(12, 2) == "12"
    assert candidate(97, 8) == "79"
    assert candidate(12, 1) == "21", "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate(11, 101) == "11", "This prints if this assert fails 2 (also good for debugging!)"


check(circular_shift)