
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
    # Step 1: Convert N to string and sum its digits.
    digit_sum = sum(int(c) for c in str(N))
    
    # Step 2: Convert the sum to binary and remove the '0b' prefix.
    binary_sum = bin(digit_sum)[2:]
    
    # Step 3: Return the binary representation as a string.
    return binary_sum

# Testing the function with provided feedback cases
print(solve(1000))  # Should return "1"
print(solve(150))   # Should return "110"
print(solve(147))   # Should return "1100"
print(solve(0))     # Should return "0"
print(solve(9999))  # Should return "10010"
print(solve(1234))  # Should return "1111"
print(solve(5005))  # Should return "1010"
print(solve(2020))  # Should return "1000"
print(solve(4321))  # Should return "1010"
print(solve(6789))  # Should return "1100"

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