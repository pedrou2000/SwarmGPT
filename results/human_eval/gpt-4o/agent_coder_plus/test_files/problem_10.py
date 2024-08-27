

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
    if string == "":
        return ""
    
    if is_palindrome(string):
        return string
    
    # Find the longest palindromic suffix
    for i in range(len(string), 0, -1):
        if is_palindrome(string[i-1:]):
            longest_palindromic_suffix = string[i-1:]
            break
    
    # The prefix that is not part of the palindromic suffix
    prefix = string[:len(string) - len(longest_palindromic_suffix)]
    
    # Reverse the prefix and append to the original string
    return string + prefix[::-1]

# Example usage
print(make_palindrome('cat'))   # Output: 'catac'
print(make_palindrome('cata'))  # Output: 'catac'
print(make_palindrome(''))      # Output: ''
print(make_palindrome('madam')) # Output: 'madam'



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