
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
    vowels = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w',
              'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}

    for char in message:
        if char in vowels:  # Check if the character is a vowel
            result.append(vowels[char])  # Replace with corresponding vowel
        elif char.isalpha():  # Check if it's a letter
            result.append(char.swapcase())  # Swap case
        else:
            result.append(char)  # Leave other characters unchanged

    return ''.join(result)  # Join the list into a single string

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)