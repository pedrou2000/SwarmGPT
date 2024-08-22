
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
    if ' ' in txt:
        return txt.split()  # Split by whitespace
    elif ',' in txt:
        return txt.split(',')  # Split by comma
    else:
        odd_lowercase_count = 0
        for char in txt:
            if 'a' <= char <= 'z':  # Check if char is a lowercase letter
                if (ord(char) - ord('a')) % 2 == 0:  # Check if position is odd (0-indexed)
                    odd_lowercase_count += 1
        return odd_lowercase_count  # Return the count of odd-positioned lowercase letters

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