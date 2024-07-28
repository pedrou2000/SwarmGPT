
def fix_spaces(text):
    """
    Given a string text, replace all spaces in it with underscores, 
    and if a string has more than 2 consecutive spaces, 
    then replace all consecutive spaces with - 
    
    fix_spaces("Example") == "Example"
    fix_spaces("Example 1") == "Example_1"
    fix_spaces(" Example 2") == "_Example_2"
    fix_spaces(" Example   3") == "_Example-3"
    """


import re

def fix_spaces(text):
    # Replace sequences of 3 or more spaces with a single hyphen
    modified_text = re.sub(r' {3,}', '-', text)
    
    # Replace single spaces with underscores
    modified_text = modified_text.replace(" ", "_")
    
    return modified_text

# Testing the function with the provided examples
print(fix_spaces("Example"))        # "Example"
print(fix_spaces("Example 1"))      # "Example_1"
print(fix_spaces(" Example 2"))     # "_Example_2"
print(fix_spaces(" Example   3"))   # "_Example-3"
print(fix_spaces("This is   a test"))  # "This_is-a_test"
print(fix_spaces("No   spaces"))    # "No-spaces"
print(fix_spaces("Multiple    spaces here"))  # "Multiple-spaces_here"
print(fix_spaces("Leading      and trailing     spaces   "))  # "_Leading-and_trailing-spaces_"

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)