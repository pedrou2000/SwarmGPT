

def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """


def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_chars = []
    for char in string:
        if char.islower():
            flipped_chars.append(char.upper())
        elif char.isupper():
            flipped_chars.append(char.lower())
        else:
            flipped_chars.append(char)  # in case there are non-alphabet characters
    return ''.join(flipped_chars)

# Example usage
print(flip_case('Hello'))  # Output: 'hELLO'
print(flip_case('Python3.8'))  # Output: 'pYTHON3.8'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('Hello!') == 'hELLO!'
    assert candidate('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

check(flip_case)