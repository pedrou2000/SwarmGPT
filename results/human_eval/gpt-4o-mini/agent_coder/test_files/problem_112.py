
def reverse_delete(s,c):
    """Task
    We are given two strings s and c, you have to deleted all the characters in s that are equal to any character in c
    then check if the result string is palindrome.
    A string is called palindrome if it reads the same backward as forward.
    You should return a tuple containing the result string and True/False for the check.
    Example
    For s = "abcde", c = "ae", the result should be ('bcd',False)
    For s = "abcdef", c = "b"  the result should be ('acdef',False)
    For s = "abcdedcba", c = "ab", the result should be ('cdedc',True)
    """


def reverse_delete(s: str, c: str) -> tuple:
    """Delete all characters in s that are equal to any character in c,
    then check if the resulting string is a palindrome.
    
    Args:
    s (str): The original string.
    c (str): The string containing characters to be deleted from s.
    
    Returns:
    tuple: A tuple containing the modified string and a boolean indicating if it's a palindrome.
    """
    result = ''.join([char for char in s if char not in c])  # Step 1: Remove characters
    is_palindrome = result == result[::-1]  # Step 2: Check for palindrome
    return (result, is_palindrome)  # Step 3: Return result

# Example test cases
print(reverse_delete("abcde", "ae"))  # Output: ('bcd', False)
print(reverse_delete("abcdef", "b"))   # Output: ('acdef', False)
print(reverse_delete("abcdedcba", "ab"))  # Output: ('cdedc', True)

def check(candidate):

    assert candidate("abcde","ae") == ('bcd',False)
    assert candidate("abcdef", "b") == ('acdef',False)
    assert candidate("abcdedcba","ab") == ('cdedc',True)
    assert candidate("dwik","w") == ('dik',False)
    assert candidate("a","a") == ('',True)
    assert candidate("abcdedcba","") == ('abcdedcba',True)
    assert candidate("abcdedcba","v") == ('abcdedcba',True)
    assert candidate("vabba","v") == ('abba',True)
    assert candidate("mamma", "mia") == ("", True)

check(reverse_delete)