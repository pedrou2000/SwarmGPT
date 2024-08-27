
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''


def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace. If no whitespaces exists in the text you
    should split on commas ','. If no commas exist, you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
    # Check if the string contains whitespace
    if ' ' in txt:
        return txt.split()
    
    # Check if the string contains commas
    if ',' in txt:
        return txt.split(',')
    
    # Count the number of lowercase letters with odd positions in the alphabet
    odd_count = 0
    for char in txt:
        if char.islower() and (ord(char) - ord('a')) % 2 == 1:
            odd_count += 1
            
    return odd_count

# Test cases
print(split_words("Hello world!"))  # ➞ ["Hello", "world!"]
print(split_words("Hello,world!"))  # ➞ ["Hello", "world!"]
print(split_words("abcdef"))        # ➞ 3
print(split_words("a quick, brown, fox"))  # ➞ ["a", "quick", "brown", "fox"]
print(split_words(""))  # ➞ 0
print(split_words(",,,,"))  # ➞ ["", "", "", ""]

def check(candidate):

    assert candidate("Hello world!") == ["Hello","world!"]
    assert candidate("Hello,world!") == ["Hello","world!"]
    assert candidate("Hello world,!") == ["Hello","world,!"]
    assert candidate("Hello,Hello,world !") == ["Hello,Hello,world","!"]
    assert candidate("abcdef") == 3
    assert candidate("aaabb") == 2
    assert candidate("aaaBb") == 1
    assert candidate("") == 0

check(split_words)