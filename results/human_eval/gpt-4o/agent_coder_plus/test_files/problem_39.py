

def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """


from math import isqrt
from itertools import islice

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def prime_fib(n: int):
    count = 0
    for fib in fibonacci_generator():
        if is_prime(fib):
            count += 1
            if count == n:
                return fib

# Test examples
print(prime_fib(1))  # Output: 2
print(prime_fib(2))  # Output: 3
print(prime_fib(3))  # Output: 5
print(prime_fib(4))  # Output: 13
print(prime_fib(5))  # Output: 89



METADATA = {}


def check(candidate):
    assert candidate(1) == 2
    assert candidate(2) == 3
    assert candidate(3) == 5
    assert candidate(4) == 13
    assert candidate(5) == 89
    assert candidate(6) == 233
    assert candidate(7) == 1597
    assert candidate(8) == 28657
    assert candidate(9) == 514229
    assert candidate(10) == 433494437


check(prime_fib)