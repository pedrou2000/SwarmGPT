
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """


from typing import List, Optional

def prod_signs(arr: List[int]) -> Optional[int]:
    """ 
    Calculate the product of signs and the sum of magnitudes of integers in the array.
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    >>> prod_signs([-1, -2, -3]) == 6
    """
    if not arr:  # Check for empty array
        return None
    
    sign_product = 1
    sum_magnitudes = 0
    
    for number in arr:
        if number > 0:
            sum_magnitudes += number
        elif number < 0:
            sum_magnitudes += -number
            sign_product *= -1
        else:
            # If there's a zero, the product of signs is zero regardless of other numbers
            return 0
    
    # If there are no non-zero numbers, return 0
    if sum_magnitudes == 0:
        return 0
    
    return sum_magnitudes * sign_product

# Example Test Cases
print(prod_signs([1, 2, 2, -4]))  # Should return -9
print(prod_signs([0, 1]))          # Should return 0
print(prod_signs([]))              # Should return None
print(prod_signs([-1, -2, -3]))    # Should return 6

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1, 2, 2, -4]) == -9
    assert candidate([0, 1]) == 0
    assert candidate([1, 1, 1, 2, 3, -1, 1]) == -10
    assert candidate([]) == None
    assert candidate([2, 4,1, 2, -1, -1, 9]) == 20
    assert candidate([-1, 1, -1, 1]) == 4
    assert candidate([-1, 1, 1, 1]) == -4
    assert candidate([-1, 1, 1, 0]) == 0

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(prod_signs)