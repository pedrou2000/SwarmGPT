
def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """


def encode(message):
    """
    Write a function that takes a message, and encodes in such a 
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the english alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """
    
    def transform_vowel(char):
        vowels = 'aeiou'
        upper_vowels = 'AEIOU'
        if char in vowels:
            return chr((ord(char) - ord('a') + 2) % 26 + ord('a')).upper()
        elif char in upper_vowels:
            return chr((ord(char) - ord('A') + 2) % 26 + ord('A')).lower()
        return char
    
    result = []
    for char in message:
        if char.isalpha():
            if char.lower() in 'aeiou':
                char = transform_vowel(char)
            else:
                char = char.swapcase()
        result.append(char)
    
    return ''.join(result)

# Testing the function with the examples provided in the docstring
print(encode('test'))  # Expected: 'TGST'
print(encode('This is a message'))  # Expected: 'tHKS KS C MGSSCGG'
print(encode('Hello World'))  # Additional test case
print(encode('Python Programming'))  # Additional test case
print(encode('abcdEFG'))  # Additional test case

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)