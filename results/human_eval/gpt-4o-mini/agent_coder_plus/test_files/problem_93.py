
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
    Encode the message by swapping case and replacing vowels. 
    """
    
    # Define the mapping for vowels
    vowel_mapping = {
        'a': 'c', 'A': 'C',
        'e': 'g', 'E': 'G',
        'i': 'k', 'I': 'K',
        'o': 'q', 'O': 'Q',
        'u': 'w', 'U': 'W'
    }
    
    result = []
    
    for char in message:
        if char in vowel_mapping:
            # Replace vowel with corresponding letter
            result.append(vowel_mapping[char])
        elif char.isalpha():
            # Swap case
            result.append(char.swapcase())
        else:
            # Keep non-letter characters unchanged
            result.append(char)
    
    return ''.join(result)

# Testing the function with the provided examples
print(encode('test'))  # Should return 'TGST'
print(encode('This is a message'))  # Should return 'tHKS KS C MGSSCGG'

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)