
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
    # Step 1: Sum the digits of N
    digit_sum = sum(int(digit) for digit in str(N))

    # Step 2: Convert the sum to a binary string and remove '0b' prefix
    binary_sum = bin(digit_sum)[2:]

    return binary_sum

# Test cases to verify the solution
print(solve(1000))  # Expected output: "1"
print(solve(150))   # Expected output: "110"
print(solve(147))   # Expected output: "1100"
print(solve(0))     # Expected output: "0"
print(solve(9999))  # Expected output: "100100"  # Corrected expected output
print(solve(1))     # Expected output: "1"
print(solve(1234))  # Expected output: "1010"    # Corrected expected output
print(solve(9876))  # Expected output: "11110"   # Corrected expected output

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