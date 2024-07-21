from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    numbers.sort()
    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) < threshold:
            return True
    return False

# Testing the function with assert statements
assert has_close_elements([1.0, 2.0, 3.0], 0.5) == False
assert has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) == True
assert has_close_elements([1.5, 1.7, 2.0, 2.4], 0.2) == True
assert has_close_elements([1.0, 1.4, 1.6, 1.7], 0.3) == True
assert has_close_elements([10, 20, 30], 5) == False
assert has_close_elements([], 1) == False  # edge case with an empty list
