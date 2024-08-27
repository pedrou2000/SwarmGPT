
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


def fix_spaces(text):
    result = []
    space_count = 0

    for c in text:
        if c == ' ':
            space_count += 1
        else:
            if space_count > 2:
                result.append('-')
            elif space_count > 0:
                result.append('_' * space_count)
            space_count = 0
            result.append(c)

    # Handle trailing spaces
    if space_count > 2:
        result.append('-')
    elif space_count > 0:
        result.append('_' * space_count)

    return ''.join(result)

# Assert-based tests
assert fix_spaces("Example") == "Example", "Test case 1 failed"
assert fix_spaces("Example 1") == "Example_1", "Test case 2 failed"
assert fix_spaces(" Example 2") == "_Example_2", "Test case 3 failed"
assert fix_spaces(" Example   3") == "_Example-3", "Test case 4 failed"
assert fix_spaces("   ") == "-", "Test case 5 failed"
assert fix_spaces("a  b") == "a__b", "Test case 6 failed"
assert fix_spaces("a    b") == "a-b", "Test case 7 failed"
assert fix_spaces(" a b ") == "_a_b_", "Test case 8 failed"

print("All test cases passed!")

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)