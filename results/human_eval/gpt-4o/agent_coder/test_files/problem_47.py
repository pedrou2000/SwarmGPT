

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
    # Step 1: Sort the list
    sorted_list = sorted(l)
    
    # Step 2: Determine the length of the list
    n = len(sorted_list)
    
    # Step 3: Calculate the median
    if n % 2 == 1:  # If the length of the list is odd
        return sorted_list[n // 2]
    else:  # If the length of the list is even
        mid1 = sorted_list[(n // 2) - 1]
        mid2 = sorted_list[n // 2]
        return (mid1 + mid2) / 2

# Example usage and testing
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