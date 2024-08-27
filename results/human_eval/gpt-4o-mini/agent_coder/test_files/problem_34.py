

def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """


def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """
    # Step 2: Remove duplicates by converting to a set
    unique_elements = set(l)
    
    # Step 3: Convert back to a list
    unique_list = list(unique_elements)
    
    # Step 4: Sort the list
    unique_list.sort()
    
    # Step 5: Return the result
    return unique_list



METADATA = {}


def check(candidate):
    assert candidate([5, 3, 5, 2, 3, 3, 9, 0, 123]) == [0, 2, 3, 5, 9, 123]


check(unique)