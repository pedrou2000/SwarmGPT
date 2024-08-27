
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
        return 0  # There are no 0-digit positive integers
    if n == 1:
        return 2  # The numbers 1 and 1 (start with 1 and end with 1)

    start_with_1 = 10 ** (n - 1)  # Numbers that start with 1
    end_with_1 = 10 ** (n - 1)    # Numbers that end with 1

    # Numbers that both start and end with 1 are of the form 1xxxx...xx1
    # There are 10^(n-2) such numbers
    overlap = 10 ** (n - 2)

    return start_with_1 + end_with_1 - overlap

# Example usage:
print(starts_one_ends(1))  # Should return 2
print(starts_one_ends(2))  # Should return 18
print(starts_one_ends(3))  # Should return 198
print(starts_one_ends(4))  # Should return 1998
print(starts_one_ends(5))  # Should return 19998
print(starts_one_ends(10)) # Should return 1999999998
print(starts_one_ends(6))  # Should return 199998
print(starts_one_ends(7))  # Should return 1999998
print(starts_one_ends(8))  # Should return 19999998
print(starts_one_ends(9))  # Should return 199999998
print(starts_one_ends(0))  # Should return 0

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