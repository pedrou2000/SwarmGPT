
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    if n == 1:
        return 2  # '1' and '1' (the only one-digit number is 1)
    
    # Count of n-digit numbers starting with 1
    start_with_1 = 10 ** (n - 1)  # 1xxxx... (n-1 zeros)
    
    # Count of n-digit numbers ending with 1
    end_with_1 = 9 * (10 ** (n - 2))  # 1 to 9 for the first digit and 0-9 for the rest
    
    # Total count of n-digit numbers that start or end with 1
    total_count = start_with_1 + end_with_1
    
    return total_count

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