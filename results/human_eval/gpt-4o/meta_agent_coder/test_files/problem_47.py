

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
    # Sort the list
    sorted_list = sorted(l)
    
    # Find the length of the list
    n = len(sorted_list)
    
    # Compute the median based on odd or even length
    if n % 2 == 1:
        # Odd case: return the middle element
        return sorted_list[n // 2]
    else:
        # Even case: return the average of the two middle elements
        middle1 = sorted_list[n // 2 - 1]
        middle2 = sorted_list[n // 2]
        return (middle1 + middle2) / 2.0

# Sample test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()



METADATA = {}


def check(candidate):
    assert candidate([3, 1, 2, 4, 5]) == 3
    assert candidate([-10, 4, 6, 1000, 10, 20]) == 8.0
    assert candidate([5]) == 5
    assert candidate([6, 5]) == 5.5
    assert candidate([8, 1, 3, 9, 9, 2, 7]) == 7 


check(median)