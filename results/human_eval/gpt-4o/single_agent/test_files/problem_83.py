
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
        return 1  # Only 1 satisfies the condition
    
    # There are 9 * 10^(n-1) n-digit numbers in total
    total_n_digit_numbers = 9 * 10**(n-1)
    
    # Numbers starting with 1: 10^(n-1)
    # Numbers ending with 1: 10^(n-1)
    # Numbers starting and ending with 1: 10^(n-2)
    
    count_starting_with_1 = 10**(n-1)
    count_ending_with_1 = 10**(n-1)
    count_starting_and_ending_with_1 = 10**(n-2)
    
    return count_starting_with_1 + count_ending_with_1 - count_starting_and_ending_with_1

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