
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
    
    Example:
        For N = 1000, the sum of digits will be 1 the output should be "1".
        For N = 150, the sum of digits will be 6 the output should be "110".
        For N = 147, the sum of digits will be 12 the output should be "1100".
    
    Variables:
        @N integer
             Constraints: 0 ≤ N ≤ 10000.
    Output:
         a string of binary number
    """
    
    # Step 1: Convert N to a string to iterate over each digit.
    digits = str(N)
    
    # Step 2: Initialize a variable to store the sum of the digits.
    digit_sum = 0
    
    # Step 3: Loop through each character in the string representation of N.
    for digit in digits:
        digit_sum += int(digit)
    
    # Step 4: Convert the sum to binary and remove the '0b' prefix.
    binary_sum = bin(digit_sum)[2:]
    
    # Step 5: Return the binary string.
    return binary_sum

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