
def check_if_last_char_is_a_letter(txt):
    '''
    Create a function that returns True if the last character
    of a given string is an alphabetical character and is not
    a part of a word, and False otherwise.
    Note: "word" is a group of characters separated by space.

    Examples:
    check_if_last_char_is_a_letter("apple pie") ➞ False
    check_if_last_char_is_a_letter("apple pi e") ➞ True
    check_if_last_char_is_a_letter("apple pi e ") ➞ False
    check_if_last_char_is_a_letter("") ➞ False 
    '''


def check_if_last_char_is_a_letter(txt):
    # Step 1: Trim the input string
    trimmed_txt = txt.rstrip()  # Strip trailing whitespace
    
    # Step 2: Check for empty string after trimming
    if not trimmed_txt:
        return False
    
    # Step 3: Get the last character
    last_char = trimmed_txt[-1]
    
    # Step 4: Check if last character is a letter and not part of a word
    if last_char.isalpha():  # Check if last character is alphabetical
        if len(trimmed_txt) > 1:  # Check if there are characters before the last one
            if trimmed_txt[-2] == ' ':  # Check if the character before it is a space
                return True
        else:  # If the string length is 1, then it's the only character
            return True
    
    # Step 5: If none of the conditions are met, return False
    return False

def check(candidate):

    # Check some simple cases
    assert candidate("apple") == False
    assert candidate("apple pi e") == True
    assert candidate("eeeee") == False
    assert candidate("A") == True
    assert candidate("Pumpkin pie ") == False
    assert candidate("Pumpkin pie 1") == False
    assert candidate("") == False
    assert candidate("eeeee e ") == False
    assert candidate("apple pie") == False
    assert candidate("apple pi e ") == False

    # Check some edge cases that are easy to work out by hand.
    assert True


check(check_if_last_char_is_a_letter)