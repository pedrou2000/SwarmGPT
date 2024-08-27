

def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """


def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """
    if len(l) <= 1:
        return True

    initial_trend = None

    for i in range(1, len(l)):
        if l[i] != l[i - 1]:
            if l[i] > l[i - 1]:
                initial_trend = "increasing"
            else:
                initial_trend = "decreasing"
            break

    if initial_trend is None:
        return True

    for i in range(1, len(l)):
        if initial_trend == "increasing" and l[i] < l[i - 1]:
            return False
        if initial_trend == "decreasing" and l[i] > l[i - 1]:
            return False

    return True



METADATA = {}


def check(candidate):
    assert candidate([1, 2, 4, 10]) == True
    assert candidate([1, 2, 4, 20]) == True
    assert candidate([1, 20, 4, 10]) == False
    assert candidate([4, 1, 0, -10]) == True
    assert candidate([4, 1, 1, 0]) == True
    assert candidate([1, 2, 3, 2, 5, 60]) == False
    assert candidate([1, 2, 3, 4, 5, 60]) == True
    assert candidate([9, 9, 9, 9]) == True


check(monotonic)