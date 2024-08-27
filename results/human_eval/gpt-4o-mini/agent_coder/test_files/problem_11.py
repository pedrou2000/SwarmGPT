from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """


from typing import List

def string_xor(a: str, b: str) -> str:
    result = []
    
    for bit_a, bit_b in zip(a, b):
        if bit_a == bit_b:
            result.append('0')
        else:
            result.append('1')

    return ''.join(result)

# Example test case
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