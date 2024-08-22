

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """


def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string. """
    n = len(string)
    
    # Find longest palindromic suffix
    for i in range(n):
        if is_palindrome(string[i:]):
            # The suffix string that is a palindrome
            suffix = string[i:]
            # The prefix string that needs to be reversed and added
            prefix = string[:i]
            return string + prefix[::-1]  # Append the reversed prefix

    # If no palindromic suffix is found, return the original string + its reverse
    return string + string[::-1]

# Test cases
print(make_palindrome(''))        # ''
print(make_palindrome('cat'))     # 'catac'
print(make_palindrome('cata'))    # 'catac'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('x') == 'x'
    assert candidate('xyz') == 'xyzyx'
    assert candidate('xyx') == 'xyx'
    assert candidate('jerry') == 'jerryrrej'

check(make_palindrome)