
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
    encoded_chars = []
    
    for char in message:
        if char.lower() in 'aeiou':
            # Replace vowel with the letter 2 places ahead
            if char == 'a':
                encoded_chars.append('c')
            elif char == 'e':
                encoded_chars.append('g')
            elif char == 'i':
                encoded_chars.append('k')
            elif char == 'o':
                encoded_chars.append('q')
            elif char == 'u':
                encoded_chars.append('w')
            elif char == 'A':
                encoded_chars.append('C')
            elif char == 'E':
                encoded_chars.append('G')
            elif char == 'I':
                encoded_chars.append('K')
            elif char == 'O':
                encoded_chars.append('Q')
            elif char == 'U':
                encoded_chars.append('W')
        elif char.isalpha():
            # Swap case
            encoded_chars.append(char.swapcase())
        else:
            # Keep non-letter characters as is
            encoded_chars.append(char)
    
    return ''.join(encoded_chars)

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)