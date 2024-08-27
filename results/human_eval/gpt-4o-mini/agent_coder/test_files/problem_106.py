
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """


def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """
    def calculate_factorial(x):
        if x == 0:
            return 1
        factorial = 1
        for j in range(1, x + 1):
            factorial *= j
        return factorial
    
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:  # i is even
            result.append(calculate_factorial(i))
        else:  # i is odd
            result.append(i * (i + 1) // 2)  # Sum of first i natural numbers

    return result

def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)