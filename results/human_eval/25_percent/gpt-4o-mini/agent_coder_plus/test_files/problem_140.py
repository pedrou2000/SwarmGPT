
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
    text = text.strip()  # Remove leading and trailing spaces
    segments = text.split(' ')  # Split by spaces
    result = []
    previous_segment = ""
    
    for segment in segments:
        if segment:  # Check if the segment is not empty
            if previous_segment:  # If there is a previous segment, add the appropriate character
                count_spaces = text.count(' ', text.index(previous_segment) + len(previous_segment), text.index(segment))
                if count_spaces > 2:
                    result.append('-')
                else:
                    result.append('_')
            result.append(segment)  # Add the current segment
            previous_segment = segment  # Update previous segment
    
    return ''.join(result)  # Join all parts into a single string

# Testing the function with provided examples
print(fix_spaces("Example"))          # Output: "Example"
print(fix_spaces("Example 1"))        # Output: "Example_1"
print(fix_spaces(" Example 2"))       # Output: "_Example_2"
print(fix_spaces(" Example   3"))     # Output: "_Example-3"

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)