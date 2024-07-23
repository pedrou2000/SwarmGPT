

def fib4(n: int):
    """The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
    fib4(0) -> 0
    fib4(1) -> 0
    fib4(2) -> 2
    fib4(3) -> 0
    fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
    Please write a function to efficiently compute the n-th element of the fib4 number sequence.  Do not use recursion.
    >>> fib4(5)
    4
    >>> fib4(6)
    8
    >>> fib4(7)
    14
    """


    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 2
    elif n == 3:
        return 0

    fib4_values = [0] * (n + 1)
    fib4_values[0] = 0
    fib4_values[1] = 0
    fib4_values[2] = 2
    fib4_values[3] = 0

    for i in range(4, n + 1):
        fib4_values[i] = (fib4_values[i - 1] + 
                          fib4_values[i - 2] + 
                          fib4_values[i - 3] + 
                          fib4_values[i - 4])

    return fib4_values[n]



METADATA = {}


def check(candidate):
    assert candidate(5) == 4
    assert candidate(8) == 28
    assert candidate(10) == 104
    assert candidate(12) == 386


check(fib4)