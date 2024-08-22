

def fib(n: int):
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """


def fib(n: int) -> int:
    """Return n-th Fibonacci number.
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1  # Initialize fib(0) and fib(1)
    
    for _ in range(2, n + 1):
        c = a + b  # Calculate the next Fibonacci number
        a = b      # Move to the next
        b = c      # Update to the latest Fibonacci number
    
    return b  # Return the n-th Fibonacci number



METADATA = {}


def check(candidate):
    assert candidate(10) == 55
    assert candidate(1) == 1
    assert candidate(8) == 21
    assert candidate(11) == 89
    assert candidate(12) == 144


check(fib)