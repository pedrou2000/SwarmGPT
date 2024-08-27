
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
    total = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            total += lst[i]
    return total

# Test example
print(add([4, 2, 6, 7]))  # Output should be 2
print(add([10, 20, 30, 40, 50, 60]))  # Output should be 60
print(add([1, 3, 5, 8, 10, 12]))  # Output should be 20 (8 from index 3 + 12 from index 5)
print(add([2, 4, 6, 8, 10, 12]))  # Output should be 24 (4 from index 1 + 8 from index 3 + 12 from index 5)

def check(candidate):

    # Check some simple cases
    assert candidate([4, 88]) == 88
    assert candidate([4, 5, 6, 7, 2, 122]) == 122
    assert candidate([4, 0, 6, 7]) == 0
    assert candidate([4, 4, 6, 8]) == 12

    # Check some edge cases that are easy to work out by hand.
    

check(add)