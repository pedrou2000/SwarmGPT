

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


def is_prime(num: int) -> bool:
    """Check if the given number is a prime number."""
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def generate_fibonacci():
    """Generator to yield Fibonacci numbers indefinitely."""
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

def prime_fib(n: int) -> int:
    """Returns the n-th number that is a Fibonacci number and also prime."""
    fib_gen = generate_fibonacci()
    count = 0
    while True:
        fib_number = next(fib_gen)
        if is_prime(fib_number):
            count += 1
            if count == n:
                return fib_number

# Example usage:
# print(prime_fib(1))  # Output: 2
# print(prime_fib(2))  # Output: 3
# print(prime_fib(3))  # Output: 5
# print(prime_fib(4))  # Output: 13
# print(prime_fib(5))  # Output: 89



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