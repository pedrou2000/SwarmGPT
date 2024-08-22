
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
    result = []
    vowels = 'aeiouAEIOU'
    
    for char in message:
        if char in vowels:
            # Calculate the letter that is two places ahead
            if char.islower():
                new_char = chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
            else:
                new_char = chr((ord(char) - ord('A') + 2) % 26 + ord('A'))
            result.append(new_char)
        else:
            # Swap case
            if char.islower():
                result.append(char.upper())
            else:
                result.append(char.lower())
    
    return ''.join(result)

# Let's test the function with the provided examples
print(encode('test'))  # Should output 'TGST'
print(encode('This is a message'))  # Should output 'tHKS KS C MGSSCGG'

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)