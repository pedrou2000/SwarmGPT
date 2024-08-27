
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
    Write a function that takes a message, and encodes it in such a 
    way that it swaps the case of all letters and replaces all vowels with 
    the letter that appears 2 places ahead in the English alphabet. 
    Assume only letters. 
    """
    vowels = 'aeiouAEIOU'
    encoded_message = []

    for char in message:
        if char in vowels:
            # Replace vowel with the letter two places ahead
            if char.islower():
                encoded_message.append(chr(ord(char) + 2))
            else:
                encoded_message.append(chr(ord(char) + 2).upper())
        else:
            # Swap case for non-vowel characters
            if char.islower():
                encoded_message.append(char.upper())
            else:
                encoded_message.append(char.lower())
    
    return ''.join(encoded_message)

# Test cases
print(encode('test'))  # Expected: 'TGST'
print(encode('This is a message'))  # Expected: 'tHKS KS C MGSSCGG'

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)