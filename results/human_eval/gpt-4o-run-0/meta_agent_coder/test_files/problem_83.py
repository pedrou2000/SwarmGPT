
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


def starts_one_ends(n):
    if n == 1:
        return 1  # Special case: single digit numbers 1
    
    count = 0
    
    # Count numbers that start with 1
    start_with_1 = 10 ** (n - 1)
    end_with_9 = start_with_1 * 2 - 1
    count += end_with_9 - start_with_1 + 1
    
    # Count numbers that end with 1 (excluding those starting with 1)
    for i in range(10 ** (n - 1), 10 ** n):
        if str(i).endswith('1') and not str(i).startswith('1'):
            count += 1
    
    return count

# Testing the function
print(starts_one_ends(1))  # Expected: 1
print(starts_one_ends(2))  # Expected: 19
print(starts_one_ends(3))  # Additional test case
print(starts_one_ends(4))  # Additional test case

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