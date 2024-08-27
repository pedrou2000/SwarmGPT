
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
        # 1-digit numbers that start or end with 1 are just the number 1 itself
        return 1
    
    # Count of n-digit numbers that start with 1
    start_with_1 = 9 * 10 ** (n - 2)
    
    # Count of n-digit numbers that end with 1
    end_with_1 = 10 ** (n - 1) // 10
    
    # Count of n-digit numbers that both start and end with 1
    start_and_end_with_1 = 10 ** (n - 2)
    
    # Total count
    total_count = start_with_1 + end_with_1 - start_and_end_with_1
    
    return total_count

# Example usage:
print(starts_one_ends(2))  # Expected output: 18

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