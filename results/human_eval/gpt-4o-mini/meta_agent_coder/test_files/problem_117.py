
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """


from typing import List

def count_consonants(word: str) -> int:
    """ Helper function to count consonants in a word. """
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for char in word if char in consonants)

def select_words(s: str, n: int) -> List[str]:
    """ Given a string s and a natural number n, return a list of all words from s
    that contain exactly n consonants. """
    if not s:  # Check if the string is empty
        return []
    
    words = s.split()  # Split the string into words
    result = []  # Initialize the result list

    for word in words:
        if count_consonants(word) == n:  # Count consonants and check
            result.append(word)  # Append to result if count matches n

    return result  # Return the result list

def check(candidate):

    # Check some simple cases
    assert candidate("Mary had a little lamb", 4) == ["little"], "First test error: " + str(candidate("Mary had a little lamb", 4))      
    assert candidate("Mary had a little lamb", 3) == ["Mary", "lamb"], "Second test error: " + str(candidate("Mary had a little lamb", 3))  
    assert candidate("simple white space", 2) == [], "Third test error: " + str(candidate("simple white space", 2))      
    assert candidate("Hello world", 4) == ["world"], "Fourth test error: " + str(candidate("Hello world", 4))  
    assert candidate("Uncle sam", 3) == ["Uncle"], "Fifth test error: " + str(candidate("Uncle sam", 3))


    # Check some edge cases that are easy to work out by hand.
    assert candidate("", 4) == [], "1st edge test error: " + str(candidate("", 4))
    assert candidate("a b c d e f", 1) == ["b", "c", "d", "f"], "2nd edge test error: " + str(candidate("a b c d e f", 1))


check(select_words)