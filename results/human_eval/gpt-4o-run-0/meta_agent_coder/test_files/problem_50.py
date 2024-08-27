

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
    """
    Takes as input a string encoded with the encode_shift function. Returns the decoded string.
    """
    decoded_chars = []
    for ch in s:
        # Calculate original character by reversing the shift
        original_char = chr(((ord(ch) - 5 - ord('a')) % 26) + ord('a'))
        decoded_chars.append(original_char)
    return ''.join(decoded_chars)

# Example usage:
encoded_string = encode_shift("hello")
print(f"Encoded: {encoded_string}")
decoded_string = decode_shift(encoded_string)
print(f"Decoded: {decoded_string}")



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