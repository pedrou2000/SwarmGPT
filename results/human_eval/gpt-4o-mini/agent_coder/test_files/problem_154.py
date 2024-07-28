
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """


def cycpattern_check(a, b):
    """Check if the second word or any of its rotations is a substring in the first word."""
    # Handle edge case where b is empty
    if not b:
        return True
    
    # Concatenate b with itself
    concatenated_b = b + b
    len_b = len(b)
    
    # Check all rotations of b
    for i in range(len_b):
        rotation = concatenated_b[i:i + len_b]  # Get the rotation
        if rotation in a:  # Check if this rotation is in a
            return True
            
    return False

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