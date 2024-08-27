

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
    index = 0
    substring_length = len(substring)
    
    # Continue until we reach the end of the string where the substring could fit
    while index <= len(string) - substring_length:
        # Check if the substring matches the part of the string
        if string[index:index + substring_length] == substring:
            count += 1  # Increment count for each found occurrence
            index += 1  # Move only one character forward to allow for overlap
        else:
            index += 1  # Move to the next character if no match
    
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