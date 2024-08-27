
def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """


def digitSum(s):
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
        digitSum("") => 0
        digitSum("abAB") => 131
        digitSum("abcCd") => 67
        digitSum("helloE") => 69
        digitSum("woArBld") => 131
        digitSum("aAaaaXa") => 153
    """
    sum_ascii = 0
    for c in s:
        if 'A' <= c <= 'Z':
            sum_ascii += ord(c)
    return sum_ascii

# Test cases
print(digitSum(""))            # Output: 0
print(digitSum("abAB"))        # Output: 131
print(digitSum("abcCd"))       # Output: 67
print(digitSum("helloE"))      # Output: 69
print(digitSum("woArBld"))     # Output: 131
print(digitSum("aAaaaXa"))     # Output: 153

# Additional test cases
print(digitSum("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))  # All uppercase letters, should sum to 2015
print(digitSum("abcdefghijklmnopqrstuvwxyz"))  # All lowercase letters, should sum to 0
print(digitSum("1234567890"))                  # Digits only, should sum to 0
print(digitSum("!@#$%^&*()"))                  # Special characters, should sum to 0
print(digitSum("aA1!Zz"))                      # Mixed characters, should sum to 156 (A + Z)

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("") == 0, "Error"
    assert candidate("abAB") == 131, "Error"
    assert candidate("abcCd") == 67, "Error"
    assert candidate("helloE") == 69, "Error"
    assert candidate("woArBld") == 131, "Error"
    assert candidate("aAaaaXa") == 153, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(" How are yOu?") == 151, "Error"
    assert candidate("You arE Very Smart") == 327, "Error"


check(digitSum)