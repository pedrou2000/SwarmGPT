
def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """


def solve(N):
    """Given a positive integer N, return the total sum of its digits in binary.
    
    Example
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    # Calculate the sum of digits
    sum_of_digits = sum(int(digit) for digit in str(N))
    
    # Convert the sum to binary and remove the '0b' prefix
    binary_representation = bin(sum_of_digits)[2:]
    
    return binary_representation

# Example usage and test cases:
print(solve(1000))  # Output: "1"
print(solve(150))   # Output: "110"
print(solve(147))   # Output: "1100"

# Additional test cases:
assert solve(1000) == "1", "Test case 1: N = 1000"
assert solve(150) == "110", "Test case 2: N = 150"
assert solve(147) == "1100", "Test case 3: N = 147"
assert solve(0) == "0", "Test case 4: N = 0"
assert solve(1234) == "1110", "Test case 5: N = 1234"
assert solve(9999) == "11000", "Test case 6: N = 9999"
assert solve(505) == "1010", "Test case 7: N = 505"
assert solve(10) == "11", "Test case 8: N = 10"
assert solve(789) == "1100", "Test case 9: N = 789"
assert solve(1111) == "100", "Test case 10: N = 1111"

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1000) == "1", "Error"
    assert candidate(150) == "110", "Error"
    assert candidate(147) == "1100", "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(333) == "1001", "Error"
    assert candidate(963) == "10010", "Error"


check(solve)