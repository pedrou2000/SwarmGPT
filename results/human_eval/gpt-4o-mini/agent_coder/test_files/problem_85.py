
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """


def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total = 0
    for index in range(1, len(lst), 2):  # Start from index 1 and step by 2 to get odd indices
        if lst[index] % 2 == 0:  # Check if the number is even
            total += lst[index]  # Add to total if it is even
    return total

def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

check(add)