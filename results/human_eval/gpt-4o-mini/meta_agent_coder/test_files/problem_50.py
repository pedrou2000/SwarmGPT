

def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """


def decode_shift(s: str) -> str:
    decoded_chars = []
    
    for ch in s:
        if 'a' <= ch <= 'z':  # Check if the character is a lowercase letter
            original_position = (ord(ch) - ord('a') - 5) % 26  # Shift back by 5
            decoded_character = chr(original_position + ord('a'))
            decoded_chars.append(decoded_character)
        else:
            decoded_chars.append(ch)  # Non-lowercase characters are added unchanged
            
    return ''.join(decoded_chars)



METADATA = {}


def check(candidate):
    from random import randint, choice
    import copy
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_shift(str)
        assert candidate(copy.deepcopy(encoded_str)) == str


check(decode_shift)