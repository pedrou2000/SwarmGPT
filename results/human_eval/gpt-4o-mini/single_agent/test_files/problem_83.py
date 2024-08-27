
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    if n == 1:
        return 2  # The numbers are 1 and 1 (only one digit, both start and end with 1)
    
    # Count of n-digit numbers that start with 1
    start_with_1 = 10**(n-1)  # The first digit is 1, the rest (n-1) digits can be 0-9
    
    # Count of n-digit numbers that end with 1
    end_with_1 = 9 * (10**(n-1))  # The last digit is 1, the first digit can be 1-9, the rest (n-2) can be 0-9
    
    # Count of n-digit numbers that both start and end with 1
    start_and_end_with_1 = 10**(n-2)  # The first digit is 1, the last digit is 1, the rest (n-2) digits can be 0-9
    
    # Total count is the sum of both counts minus the intersection (to avoid double counting)
    return start_with_1 + end_with_1 - start_and_end_with_1

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