
def next_smallest(lst):
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """


def next_smallest(lst):
    """Returns the second smallest element in the list or None if it doesn't exist."""
    if len(lst) < 2:
        return None
    
    # Remove duplicates by converting to a set and back to a list
    distinct_lst = list(set(lst))
    
    # If we still have less than 2 distinct elements, return None
    if len(distinct_lst) < 2:
        return None
    
    # Sort the list
    distinct_lst.sort()
    
    # Return the second smallest element
    return distinct_lst[1]

def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4, 5]) == 2
    assert candidate([5, 1, 4, 3, 2]) == 2
    assert candidate([]) == None
    assert candidate([1, 1]) == None
    assert candidate([1,1,1,1,0]) == 1
    assert candidate([1, 0**0]) == None
    assert candidate([-35, 34, 12, -45]) == -35

    # Check some edge cases that are easy to work out by hand.
    assert True


check(next_smallest)