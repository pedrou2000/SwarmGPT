
def anti_shuffle(s):
    """
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """


def anti_shuffle(s: str) -> str:
    """ Returns an ordered version of the input string where all words are sorted 
    based on ASCII values of their characters, keeping the order of words and spaces.
    >>> anti_shuffle('Hi')
    'Hi'
    >>> anti_shuffle('hello')
    'ehllo'
    >>> anti_shuffle('Hello World!!!')
    'Hello !!!Wdlor'
    """
    # Split the input string while keeping spaces intact
    words = s.split(' ')
    
    # Sort each word and store results in a new list
    sorted_words = [''.join(sorted(word)) for word in words]
    
    # Join the sorted words back with spaces
    result = ' '.join(sorted_words)
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate('Hi') == 'Hi'
    assert candidate('hello') == 'ehllo'
    assert candidate('number') == 'bemnru'
    assert candidate('abcd') == 'abcd'
    assert candidate('Hello World!!!') == 'Hello !!!Wdlor'
    assert candidate('') == ''
    assert candidate('Hi. My name is Mister Robot. How are you?') == '.Hi My aemn is Meirst .Rboot How aer ?ouy'
    # Check some edge cases that are easy to work out by hand.
    assert True


check(anti_shuffle)