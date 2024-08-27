
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """


def cycpattern_check(a: str, b: str) -> bool:
    """Check if any rotation of b is a substring of a."""
    b_rotated = b + b  # Concatenate b with itself to generate all rotations
    return any(b_rotated[i:i+len(b)] in a for i in range(len(b)))  # Check for each rotation

# Testing the function with provided examples
print(cycpattern_check("abcd","abd"))      # False
print(cycpattern_check("hello","ell"))     # True
print(cycpattern_check("whassup","psus"))  # False
print(cycpattern_check("abab","baa"))      # True
print(cycpattern_check("efef","eeff"))     # False
print(cycpattern_check("himenss","simen")) # True

def check(candidate):

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  candidate("xyzw","xyw") == False , "test #0"
    assert  candidate("yello","ell") == True , "test #1"
    assert  candidate("whattup","ptut") == False , "test #2"
    assert  candidate("efef","fee") == True , "test #3"
    assert  candidate("abab","aabb") == False , "test #4"
    assert  candidate("winemtt","tinem") == True , "test #5"


check(cycpattern_check)