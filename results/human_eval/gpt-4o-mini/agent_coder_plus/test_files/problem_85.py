
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices..


    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """


def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.
    
    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    total_sum = 0
    
    for index, value in enumerate(lst):
        if index % 2 == 1:  # Check if the index is odd
            if value % 2 == 0:  # Check if the value is even
                total_sum += value
                
    return total_sum

def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

check(add)