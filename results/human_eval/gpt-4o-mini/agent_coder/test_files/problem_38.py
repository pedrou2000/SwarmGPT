

def encode_cyclic(s: str):
    """
    returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))] for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group) == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str):
    """
    takes as input string encoded with encode_cyclic function. Returns decoded string.
    """


def decode_cyclic(s: str) -> str:
    """ Decodes a string that was encoded with the encode_cyclic function. """

    # Split the string into groups of three characters
    groups = [s[i:i + 3] for i in range(0, len(s), 3)]
    
    # Decode each group
    decoded_groups = []
    for group in groups:
        if len(group) > 0:
            # Move the first character to the end of the group
            decoded_groups.append(group[1:] + group[0])
        else:
            # Keep the group as is (not really needed since groups are always non-empty)
            decoded_groups.append(group)

    # Join all groups to form the decoded string
    return ''.join(decoded_groups)

# Example usage:
# result = decode_cyclic("cbaefhij")
# print(result)  # Expected output: "bcaefhij"



METADATA = {}


def check(candidate):
    from random import randint, choice
    import string

    letters = string.ascii_lowercase
    for _ in range(100):
        str = ''.join(choice(letters) for i in range(randint(10, 20)))
        encoded_str = encode_cyclic(str)
        assert candidate(encoded_str) == str


check(decode_cyclic)