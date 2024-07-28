

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """


def median(l: list):
    """Return median of elements in the list l."""
    # Sort the list
    l.sort()
    n = len(l)  # Get the length of the list

    if n % 2 == 1:  # If the number of elements is odd
        return l[n // 2]  # Return the middle element
    else:  # If the number of elements is even
        return (l[n // 2 - 1] + l[n // 2]) / 2  # Return the average of the two middle elements



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)