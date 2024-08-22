

def how_many_times(string: str, substring: str) -> int:
    """ Find how many times a given substring can be found in the original string. Count overlaping cases.
    >>> how_many_times('', 'a')
    0
    >>> how_many_times('aaa', 'a')
    3
    >>> how_many_times('aaaa', 'aa')
    3
    """


def how_many_times(string: str, substring: str) -> int:
    count = 0
    string_length = len(string)
    substring_length = len(substring)

    # Edge case: If substring is empty, return 0
    if substring_length == 0:
        return 0
    
    # Loop through the string
    for i in range(string_length - substring_length + 1):
        # Check if the substring matches
        if string[i:i + substring_length] == substring:
            count += 1  # Increment count if a match is found

    return count



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('', 'x') == 0
    assert candidate('xyxyxyx', 'x') == 4
    assert candidate('cacacacac', 'cac') == 4
    assert candidate('john doe', 'john') == 1

check(how_many_times)