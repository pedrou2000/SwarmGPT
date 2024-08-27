

def fibfib(n: int):
    """The FibFib number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    Please write a function to efficiently compute the n-th element of the fibfib number sequence.
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """


def fibfib(n: int) -> int:
    """Compute the n-th element of the FibFib number sequence."""
    if n == 0 or n == 1:
        return 0
    elif n == 2:
        return 1

    # Initialize the first three FibFib numbers
    a, b, c = 0, 0, 1  # fibfib(0), fibfib(1), fibfib(2)

    # Compute FibFib numbers from 3 to n
    for i in range(3, n + 1):
        # fibfib(n) = fibfib(n-1) + fibfib(n-2) + fibfib(n-3)
        fibfib_n = a + b + c
        # Update the variables for the next iteration
        a, b, c = b, c, fibfib_n

    return c  # c holds the value of fibfib(n)

# Test cases
print(fibfib(1))  # Output: 0
print(fibfib(5))  # Output: 4
print(fibfib(8))  # Output: 24



METADATA = {}


def check(candidate):
    assert candidate(2) == 1
    assert candidate(1) == 0
    assert candidate(5) == 4
    assert candidate(8) == 24
    assert candidate(10) == 81
    assert candidate(12) == 274
    assert candidate(14) == 927


check(fibfib)