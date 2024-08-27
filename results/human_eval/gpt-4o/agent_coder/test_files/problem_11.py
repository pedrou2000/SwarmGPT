from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    
    # Ensure both strings are of the same length
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")
    
    for i in range(len(a)):
        xor_result = int(a[i]) ^ int(b[i])
        result += str(xor_result)
    
    return result

# Example usage and testing
if __name__ == "__main__":
    print(string_xor('010', '110'))  # Output should be '100'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('111000', '101010') == '010010'
    assert candidate('1', '1') == '0'
    assert candidate('0101', '0000') == '0101'

check(string_xor)