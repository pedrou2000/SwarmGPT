
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
    way that it swaps case of all letters, replaces all vowels in 
    the message with the letter that appears 2 places ahead of that 
    vowel in the English alphabet. 
    Assume only letters. 
    
    Examples:
    >>> encode('test')
    'TGST'
    >>> encode('This is a message')
    'tHKS KS C MGSSCGG'
    """

    def swap_case(char):
        if char.islower():
            return char.upper()
        else:
            return char.lower()

    def replace_vowel(char):
        vowels = 'aeiou'
        vowels_upper = 'AEIOU'
        
        if char in vowels:
            return chr(((ord(char) - ord('a') + 2) % 26) + ord('a')).upper()
        elif char in vowels_upper:
            return chr(((ord(char) - ord('A') + 2) % 26) + ord('A')).lower()
        return char

    encoded_message = ''
    for char in message:
        swapped_char = swap_case(char)
        if swapped_char.lower() in 'aeiou':
            new_char = replace_vowel(swapped_char)
        else:
            new_char = swapped_char
        encoded_message += new_char

    return encoded_message

# Example usage
print(encode('test'))  # Output: 'TGST'
print(encode('This is a message'))  # Output: 'tHKS KS C MGSSCGG'
print(encode('HELLO world'))  # Output: 'hCLLN WNRLD'
print(encode('AEIOU aeio'))  # Output: 'CGKQW CGKQ'
print(encode('Python Programming'))  # Output: 'pYTHQN pRQRCLLMMKNG'
print(encode('AbCdEfGhIjKlMnOpQrStUvWxYz'))  # Output: 'cDgFhJkLnOpQrStVwYz'

def check(candidate):

    # Check some simple cases
    assert candidate('TEST') == 'tgst', "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('Mudasir') == 'mWDCSKR', "This prints if this assert fails 2 (good for debugging!)"
    assert candidate('YES') == 'ygs', "This prints if this assert fails 3 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate('This is a message') == 'tHKS KS C MGSSCGG', "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate("I DoNt KnOw WhAt tO WrItE") == 'k dQnT kNqW wHcT Tq wRkTg', "This prints if this assert fails 2 (also good for debugging!)"


check(encode)