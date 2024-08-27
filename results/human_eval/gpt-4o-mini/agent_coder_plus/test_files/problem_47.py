

def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """


def median(l: list):
    """Return median of elements in the list l.
    >>> median([3, 1, 2, 4, 5])
    3
    >>> median([-10, 4, 6, 1000, 10, 20])
    15.0
    """
    if not l:  # Check if the list is empty
        return None
    
    l.sort()  # Sort the list
    length = len(l)  # Get the length of the list
    
    if length % 2 == 1:  # If the length is odd
        return l[length // 2]  # Middle element
    else:  # If the length is even
        return (l[length // 2 - 1] + l[length // 2]) / 2  # Average of the two middle elements



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)