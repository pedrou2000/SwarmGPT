
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


from typing import List, Optional

def next_smallest(lst: List[int]) -> Optional[int]:
    """ 
    Return the second smallest element of the list.
    Return None if there is no such element.
    """
    if not lst:  # Check for empty list
        return None
    
    unique_elements = set(lst)  # Remove duplicates
    if len(unique_elements) < 2:  # Check if there are at least 2 distinct elements
        return None
    
    sorted_elements = sorted(unique_elements)  # Sort the unique elements
    return sorted_elements[1]  # Return the second smallest element

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