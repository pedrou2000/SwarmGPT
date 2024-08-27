

def is_palindrome(text: str):
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """


def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    >>> is_palindrome('')
    True
    >>> is_palindrome('aba')
    True
    >>> is_palindrome('aaaaa')
    True
    >>> is_palindrome('zbcd')
    False
    """
    # Step 1: Handle the empty string case
    if not text:
        return True
    
    # Step 2: Normalize the string to lower case
    text = text.lower()
    
    # Step 3: Initialize pointers
    left, right = 0, len(text) - 1
    
    # Step 4: Check for palindrome
    while left < right:
        if text[left] != text[right]:
            return False
        left += 1
        right -= 1
    
    # Step 5: If all characters matched, it is a palindrome
    return True



METADATA = {}


def check(candidate):
    assert candidate('') == True
    assert candidate('aba') == True
    assert candidate('aaaaa') == True
    assert candidate('zbcd') == False
    assert candidate('xywyx') == True
    assert candidate('xywyz') == False
    assert candidate('xywzx') == False


check(is_palindrome)