
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
    """Return the second smallest element from the list, or None if it does not exist."""
    if not lst:  # Check if the list is empty
        return None

    unique_elements = set(lst)  # Remove duplicates
    sorted_unique_elements = sorted(unique_elements)  # Sort the unique elements
    
    if len(sorted_unique_elements) < 2:  # Check if we have at least two unique elements
        return None
    
    return sorted_unique_elements[1]  # Return the second smallest element

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