
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


def anti_shuffle(s):
    """ 
    Write a function that takes a string and returns an ordered version of it.
    Ordered version of string, is a string where all words (separated by space)
    are replaced by a new word where all the characters arranged in
    ascending order based on ascii value.
    Note: You should keep the order of words and blank spaces in the sentence.
    
    >>> anti_shuffle('Hi')
    'Hi'
    >>> anti_shuffle('hello')
    'ehllo'
    >>> anti_shuffle('Hello World!!!')
    'Hello !!!Wdlor'
    """
    result = []
    words = s.split(' ')  # Split by spaces to preserve them
    
    for word in words:
        if word:  # If the word is not empty
            sorted_word = ''.join(sorted(word))  # Sort characters
            result.append(sorted_word)  # Add sorted word to result
        else:
            result.append(' ')  # Preserve spaces
    
    return ''.join(result)  # Join the list into a single string

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