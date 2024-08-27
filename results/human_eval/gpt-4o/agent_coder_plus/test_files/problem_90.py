
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
    """
    You are given a list of integers.
    Write a function next_smallest() that returns the 2nd smallest element of the list.
    Return None if there is no such element.
    
    next_smallest([1, 2, 3, 4, 5]) == 2
    next_smallest([5, 1, 4, 3, 2]) == 2
    next_smallest([]) == None
    next_smallest([1, 1]) == None
    """
    # Edge case: if the list has fewer than 2 elements, return None
    if len(lst) < 2:
        return None

    # Remove duplicates by converting the list to a set
    unique_elements = set(lst)

    # Edge case: if there are fewer than 2 unique elements, return None
    if len(unique_elements) < 2:
        return None

    # Convert the set back to a list and sort it
    sorted_elements = sorted(unique_elements)

    # Return the second smallest element
    return sorted_elements[1]

# Example tests
print(next_smallest([1, 2, 3, 4, 5])) # Should return 2
print(next_smallest([5, 1, 4, 3, 2])) # Should return 2
print(next_smallest([])) # Should return None
print(next_smallest([1, 1])) # Should return None

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