
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


def unique_digits(x):
    """Given a list of positive integers x, return a sorted list of all 
    elements that haven't any even digit.
    
    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    # List to store numbers without any even digits
    valid_numbers = []
    
    # Iterate through each number in the list
    for number in x:
        number_str = str(number)
        has_even_digit = False
        
        # Check if the number contains any even digit
        for digit in number_str:
            if digit in '02468':
                has_even_digit = True
                break
                
        # If no even digit is found, add the number to the list
        if not has_even_digit:
            valid_numbers.append(number)
    
    # Sort the list of valid numbers
    valid_numbers.sort()
    
    # Return the sorted list
    return valid_numbers

def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(unique_digits)