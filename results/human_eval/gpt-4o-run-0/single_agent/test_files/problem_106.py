
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
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result

    def sum_of_numbers(x):
        return x * (x + 1) // 2

    result_list = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result_list.append(factorial(i))
        else:
            result_list.append(sum_of_numbers(i))
    
    return result_list

def check(candidate):

    assert candidate(5) == [1, 2, 6, 24, 15]
    assert candidate(7) == [1, 2, 6, 24, 15, 720, 28]
    assert candidate(1) == [1]
    assert candidate(3) == [1, 2, 6]

check(f)