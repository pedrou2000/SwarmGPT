
def count_upper(s):
    """
    Given a string s, count the number of uppercase vowels in even indices.
    
    For example:
    count_upper('aBCdEf') returns 1
    count_upper('abcdefg') returns 0
    count_upper('dBBE') returns 0
    """


def count_upper(s):
    """ Given a string s, count the number of uppercase vowels in even indices. """
    count = 0
    # Iterate through the string, checking characters at even indices
    for index in range(0, len(s), 2):  # Start at 0 and step by 2 for even indices
        if s[index] in 'AEIOU':  # Check if the character is an uppercase vowel
            count += 1  # Increment the count
    return count

def check(candidate):

    # Check some simple cases
    assert candidate('aBCdEf')  == 1
    assert candidate('abcdefg') == 0
    assert candidate('dBBE') == 0
    assert candidate('B')  == 0
    assert candidate('U')  == 1
    assert candidate('') == 0
    assert candidate('EEEE') == 2

    # Check some edge cases that are easy to work out by hand.
    assert True


check(count_upper)