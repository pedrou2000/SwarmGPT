

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """


def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    1
    >>> fizz_buzz(79)
    1
    >>> fizz_buzz(100)
    1
    >>> fizz_buzz(1)
    0
    >>> fizz_buzz(11)
    0
    >>> fizz_buzz(14)
    0
    >>> fizz_buzz(77)
    1
    >>> fizz_buzz(200)
    2
    >>> fizz_buzz(0)
    0
    """
    counter = 0
    for number in range(n):
        if number % 11 == 0 or number % 13 == 0:
            counter += str(number).count('7')
    return counter



METADATA = {}


def check(candidate):
    assert candidate(50) == 0
    assert candidate(78) == 2
    assert candidate(79) == 3
    assert candidate(100) == 3
    assert candidate(200) == 6
    assert candidate(4000) == 192
    assert candidate(10000) == 639
    assert candidate(100000) == 8026


check(fizz_buzz)