

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """


def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    >>> largest_divisor(100)
    50
    >>> largest_divisor(49)
    7
    """
    for d in range(n-1, 0, -1):
        if n % d == 0:
            return d

    # This line is theoretically unreachable for n > 1
    return 1  # if n is 1, it has no divisors other than itself

# Example usage:
# print(largest_divisor(15))  # Should return 5
# print(largest_divisor(100))  # Should return 50
# print(largest_divisor(49))  # Should return 7



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3) == 1
    assert candidate(7) == 1
    assert candidate(10) == 5
    assert candidate(100) == 50
    assert candidate(49) == 7

check(largest_divisor)