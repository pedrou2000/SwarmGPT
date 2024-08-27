
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
        return 1  # The only 1-digit number starting or ending with 1 is 1 itself.

    # Calculate the count of n-digit numbers that start with 1
    count_start_1 = 10**(n-1)  # There are 10^(n-1) numbers starting with 1, from 10^(n-1) to 10^n - 1.

    # Calculate the count of n-digit numbers that end with 1
    count_end_1 = 9 * 10**(n-1)  # Every 10th number in the range is ending with 1.

    # Calculate the count of n-digit numbers that start and end with 1
    count_start_end_1 = 10**(n-2)  # There are 10^(n-2) numbers starting and ending with 1.

    # Total count is the sum of the two counts minus the overlap of numbers that start and end with 1.
    total_count = count_start_1 + count_end_1 - count_start_end_1
    return total_count

# Example usage:
# print(starts_one_ends(2))  # Should return 18

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