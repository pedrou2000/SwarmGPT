
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
    if n == 1:
        # For single-digit numbers, the numbers are 1, 2, ..., 9
        # The numbers '1' and '1' (which are the same) count as 2 cases
        return 2

    # Calculate the count of numbers that start with '1'
    start_with_1_count = 10 ** (n - 1)

    # Calculate the count of numbers that end with '1'
    end_with_1_count = 10 ** (n - 1)

    # Calculate the count of numbers that both start and end with '1'
    start_and_end_with_1_count = 10 ** (n - 2)

    # Total count is the sum of the two counts minus the overlap
    total_count = start_with_1_count + end_with_1_count - start_and_end_with_1_count

    return total_count

# Example Usage:
print(starts_one_ends(1))  # Output: 2
print(starts_one_ends(2))  # Output: 19
print(starts_one_ends(3))  # Output: 190

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