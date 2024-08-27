
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

    For example:
    anti_shuffle('Hi') returns 'Hi'
    anti_shuffle('hello') returns 'ehllo'
    anti_shuffle('Hello World!!!') returns 'Hello !!!Wdlor'
    """

    # Split the input string into parts of words and spaces
    parts = []
    word = ''
    
    for char in s:
        if char.isspace():
            if word:
                parts.append(word)
                word = ''
            parts.append(char)
        else:
            word += char
    
    if word:
        parts.append(word)
    
    # Sort each word and leave spaces unchanged
    for i in range(len(parts)):
        if not parts[i].isspace():
            parts[i] = ''.join(sorted(parts[i]))
    
    # Join the parts back together to form the final string
    return ''.join(parts)

# Example usage:
print(anti_shuffle('Hi'))            # Output: 'Hi'
print(anti_shuffle('hello'))         # Output: 'ehllo'
print(anti_shuffle('Hello World!!!')) # Output: 'Hello !!!Wdlor'

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