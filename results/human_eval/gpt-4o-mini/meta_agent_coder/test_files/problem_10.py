

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
    
    # Find the longest palindromic suffix
    for i in range(n):
        if is_palindrome(string[i:]):
            # The suffix starting from index i is a palindrome
            palindromic_suffix_index = i
            break
    else:
        # If no palindromic suffix was found, we will set it to n
        palindromic_suffix_index = n

    # Take the prefix that comes before the palindromic suffix
    prefix = string[:palindromic_suffix_index]
    # Reverse the prefix
    reversed_prefix = prefix[::-1]

    # Construct the palindrome
    return string + reversed_prefix

# Example Usage
print(make_palindrome('cat'))  # Output: 'catac'
print(make_palindrome('cata')) # Output: 'catac'
print(make_palindrome(''))      # Output: ''



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