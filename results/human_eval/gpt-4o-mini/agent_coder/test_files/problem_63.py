

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
    """The FibFib number sequence is a sequence similar to the Fibonacci sequence that's defined as follows:
    fibfib(0) == 0
    fibfib(1) == 0
    fibfib(2) == 1
    fibfib(n) == fibfib(n-1) + fibfib(n-2) + fibfib(n-3).
    >>> fibfib(1)
    0
    >>> fibfib(5)
    4
    >>> fibfib(8)
    24
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    # Dynamic programming array to store results
    fibfib_values = [0] * (n + 1)
    fibfib_values[0] = 0
    fibfib_values[1] = 0
    fibfib_values[2] = 1

    # Fill the array using the recurrence relation
    for i in range(3, n + 1):
        fibfib_values[i] = fibfib_values[i - 1] + fibfib_values[i - 2] + fibfib_values[i - 3]

    return fibfib_values[n]



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