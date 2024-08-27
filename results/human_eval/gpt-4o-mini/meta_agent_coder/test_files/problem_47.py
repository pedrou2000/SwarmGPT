

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
    if not l:  # Check for an empty list
        return None
    
    l.sort()  # Sort the list
    n = len(l)  # Get the length of the list
    
    if n % 2 == 1:  # If odd length
        return l[n // 2]  # Return the middle element
    else:  # If even length
        return (l[n // 2 - 1] + l[n // 2]) / 2  # Return the average of the two middle elements



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)