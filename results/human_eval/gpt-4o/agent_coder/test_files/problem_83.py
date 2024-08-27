
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    if n == 1:
        # Handle the special case for single-digit numbers
        return 1  # Only 1

    # Numbers starting with 1
    start_with_1 = 10**(n-1)

    # Numbers ending with 1
    end_with_1 = 9 * 10**(n-2)  # All n-digit numbers ending in 1

    # Overlap: Numbers that start and end with 1
    start_and_end_with_1 = 10**(n-2)

    # Total count of numbers that start or end with 1
    total_count = start_with_1 + end_with_1 - start_and_end_with_1

    return total_count

# Example usage:
print(starts_one_ends(2))  # Expected output: 18
print(starts_one_ends(3))  # Expected output: 180

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(starts_one_ends)