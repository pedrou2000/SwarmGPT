

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
    """ Helper function to check if a number is prime. """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_fib(n: int) -> int:
    """ Return the n-th Fibonacci number that is also prime. """
    prime_fib_numbers = []
    a, b = 0, 1

    while len(prime_fib_numbers) < n:
        a, b = b, a + b  # Generate next Fibonacci number
        if is_prime(a):
            prime_fib_numbers.append(a)

    return prime_fib_numbers[n - 1]  # Return the n-th prime Fibonacci number



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