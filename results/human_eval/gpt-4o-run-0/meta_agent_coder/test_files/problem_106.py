
def f(n):
    """ Implement the function f that takes n as a parameter,
    and returns a list of size n, such that the value of the element at index i is the factorial of i if i is even
    or the sum of numbers from 1 to i otherwise.
    i starts from 1.
    the factorial of i is the multiplication of the numbers from 1 to i (1 * 2 * ... * i).
    Example:
    f(5) == [1, 2, 6, 24, 15]
    """


def factorial(num):
    """Helper function to compute the factorial of a number."""
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

def f(n):
    """Function to return a list where the value at index i is the factorial of i if i is even,
    or the sum of numbers from 1 to i otherwise."""
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:  # i is even
            result.append(factorial(i))
        else:  # i is odd
            result.append(sum(range(1, i + 1)))
    return result

# Example usage:
print(f(5))  # Output: [1, 2, 6, 24, 15]

def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)