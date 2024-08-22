
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions.
    

    Examples
    solution([5, 8, 7, 1]) ==> 12
    solution([3, 3, 3, 3, 3]) ==> 9
    solution([30, 13, 24, 321]) ==>0
    """


def solution(lst):
    total_sum = 0
    
    for i in range(len(lst)):
        if i % 2 == 0:  # i is an even index
            if lst[i] % 2 != 0:  # lst[i] is odd
                total_sum += lst[i]
    
    return total_sum

def check(candidate):

    # Check some simple cases
    assert candidate([5, 8, 7, 1])    == 12
    assert candidate([3, 3, 3, 3, 3]) == 9
    assert candidate([30, 13, 24, 321]) == 0
    assert candidate([5, 9]) == 5
    assert candidate([2, 4, 8]) == 0
    assert candidate([30, 13, 23, 32]) == 23
    assert candidate([3, 13, 2, 9]) == 3

    # Check some edge cases that are easy to work out by hand.


check(solution)