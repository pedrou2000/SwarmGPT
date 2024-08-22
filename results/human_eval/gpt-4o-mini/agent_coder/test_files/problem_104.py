
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """


from typing import List

def unique_digits(x: List[int]) -> List[int]:
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.
    
    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    result = []
    
    for number in x:
        str_number = str(number)
        is_unique = True
        
        for digit in str_number:
            if digit in '02468':
                is_unique = False
                break
                
        if is_unique:
            result.append(number)
    
    return sorted(result)

# Example usage
print(unique_digits([15, 33, 1422, 1]))  # Output: [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # Output: []

def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(unique_digits)