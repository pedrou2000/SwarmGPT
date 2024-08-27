
def solve(s):
    """You are given a string s.
    if s[i] is a letter, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no letters, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("ab") = "AB"
    solve("#a@C") = "#A@c"
    """


def solve(s):
    result = []
    has_letter = False

    for char in s:
        if char.isalpha():  # Check if the character is a letter
            has_letter = True
            if char.islower():
                result.append(char.upper())  # Change lowercase to uppercase
            else:
                result.append(char.lower())   # Change uppercase to lowercase
        else:
            result.append(char)  # Keep non-letter characters unchanged

    if not has_letter:
        return s[::-1]  # Reverse the string if no letters were found

    return ''.join(result)  # Join the list into a string and return

def check(candidate):

    # Check some simple cases
    assert candidate("AsDf") == "aSdF"
    assert candidate("1234") == "4321"
    assert candidate("ab") == "AB"
    assert candidate("#a@C") == "#A@c"
    assert candidate("#AsdfW^45") == "#aSDFw^45"
    assert candidate("#6@2") == "2@6#"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("#$a^D") == "#$A^d"
    assert candidate("#ccc") == "#CCC"

    # Don't remove this line:

check(solve)