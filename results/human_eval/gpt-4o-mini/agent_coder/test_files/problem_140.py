
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
    # Trim the text to remove leading and trailing spaces
    text = text.strip()
    
    # If the trimmed text is empty, return an empty string
    if not text:
        return ""
    
    result = []
    
    # Split the text by whitespace (this handles multiple spaces correctly)
    parts = text.split()
    
    # Iterate through the parts
    for i, part in enumerate(parts):
        if i > 0:  # If it's not the first part, we need to add a separator
            # Check how many spaces were between the last and current part
            previous_space_count = text.find(part) - (text.find(parts[i-1]) + len(parts[i-1]))
            if previous_space_count == 1:
                result.append('_')
            elif previous_space_count > 1:
                result.append('-')
        
        # Append the current part
        result.append(part)
    
    # Join the result list into a single string
    return ''.join(result)

# Testing the function with provided test cases
print(fix_spaces("Example"))      # Expected: "Example"
print(fix_spaces("Example 1"))    # Expected: "Example_1"
print(fix_spaces(" Example 2"))   # Expected: "_Example_2"
print(fix_spaces(" Example   3"))  # Expected: "_Example-3"
print(fix_spaces("   Leading spaces")) # Expected: "-Leading_spaces"
print(fix_spaces("Trailing spaces   ")) # Expected: "Trailing_spaces-"
print(fix_spaces("Multiple    spaces    here")) # Expected: "Multiple-spaces-here"
print(fix_spaces("NoSpacesHere"))  # Expected: "NoSpacesHere"
print(fix_spaces(""))               # Expected: ""

def check(candidate):

    # Check some simple cases
    assert candidate("Example") == "Example", "This prints if this assert fails 1 (good for debugging!)"
    assert candidate("Mudasir Hanif ") == "Mudasir_Hanif_", "This prints if this assert fails 2 (good for debugging!)"
    assert candidate("Yellow Yellow  Dirty  Fellow") == "Yellow_Yellow__Dirty__Fellow", "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate("Exa   mple") == "Exa-mple", "This prints if this assert fails 4 (good for debugging!)"
    assert candidate("   Exa 1 2 2 mple") == "-Exa_1_2_2_mple", "This prints if this assert fails 4 (good for debugging!)"


check(fix_spaces)