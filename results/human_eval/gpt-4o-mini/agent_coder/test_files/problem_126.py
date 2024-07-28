
def is_sorted(lst):
    '''
    Given a list of numbers, return whether or not they are sorted
    in ascending order. If list has more than 1 duplicate of the same
    number, return False. Assume no negative numbers and only integers.

    Examples
    is_sorted([5]) ➞ True
    is_sorted([1, 2, 3, 4, 5]) ➞ True
    is_sorted([1, 3, 2, 4, 5]) ➞ False
    is_sorted([1, 2, 3, 4, 5, 6]) ➞ True
    is_sorted([1, 2, 3, 4, 5, 6, 7]) ➞ True
    is_sorted([1, 3, 2, 4, 5, 6, 7]) ➞ False
    is_sorted([1, 2, 2, 3, 3, 4]) ➞ True
    is_sorted([1, 2, 2, 2, 3, 4]) ➞ False
    '''


def is_sorted(lst):
    if not lst:  # Step 1: Check for empty list
        return True

    last_number = None
    seen_numbers = set()  # Step 2: Initialize a set for seen numbers

    for number in lst:  # Step 3: Iterate through the list
        if last_number is not None and number < last_number:  # Check if sorted
            return False
        if number in seen_numbers:  # Check for duplicates
            return False
        seen_numbers.add(number)  # Add current number to the seen set
        last_number = number  # Update last_number

    return True  # Step 4: Return True if all checks passed

def check(candidate):

    # Check some simple cases
    assert candidate([5]) == True
    assert candidate([1, 2, 3, 4, 5]) == True
    assert candidate([1, 3, 2, 4, 5]) == False
    assert candidate([1, 2, 3, 4, 5, 6]) == True
    assert candidate([1, 2, 3, 4, 5, 6, 7]) == True
    assert candidate([1, 3, 2, 4, 5, 6, 7]) == False, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([]) == True, "This prints if this assert fails 2 (good for debugging!)"
    assert candidate([1]) == True, "This prints if this assert fails 3 (good for debugging!)"
    assert candidate([3, 2, 1]) == False, "This prints if this assert fails 4 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate([1, 2, 2, 2, 3, 4]) == False, "This prints if this assert fails 5 (good for debugging!)"
    assert candidate([1, 2, 3, 3, 3, 4]) == False, "This prints if this assert fails 6 (good for debugging!)"
    assert candidate([1, 2, 2, 3, 3, 4]) == True, "This prints if this assert fails 7 (good for debugging!)"
    assert candidate([1, 2, 3, 4]) == True, "This prints if this assert fails 8 (good for debugging!)"


check(is_sorted)