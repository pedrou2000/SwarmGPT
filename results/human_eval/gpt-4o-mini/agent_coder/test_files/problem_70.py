
def strange_sort_list(lst):
    '''
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.

    Examples:
    strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
    strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    strange_sort_list([]) == []
    '''


from typing import List

def strange_sort_list(lst: List[int]) -> List[int]:
    """ 
    Given list of integers, return list in strange order.
    Strange sorting, is when you start with the minimum value,
    then maximum of the remaining integers, then minimum and so on.
    """
    if not lst:
        return []

    # Step 1: Sort the list
    lst.sort()
    
    result = []
    min_index = 0
    max_index = len(lst) - 1

    # Step 2-4: Alternate picking of min and max
    while min_index <= max_index:
        if min_index == max_index:
            result.append(lst[min_index])  # Add the last middle element if odd length
        else:
            result.append(lst[min_index])  # Add the minimum
            result.append(lst[max_index])  # Add the maximum
        
        min_index += 1
        max_index -= 1

    return result

def check(candidate):

    # Check some simple cases
    assert candidate([1, 2, 3, 4]) == [1, 4, 2, 3]
    assert candidate([5, 6, 7, 8, 9]) == [5, 9, 6, 8, 7]
    assert candidate([1, 2, 3, 4, 5]) == [1, 5, 2, 4, 3]
    assert candidate([5, 6, 7, 8, 9, 1]) == [1, 9, 5, 8, 6, 7]
    assert candidate([5, 5, 5, 5]) == [5, 5, 5, 5]
    assert candidate([]) == []
    assert candidate([1,2,3,4,5,6,7,8]) == [1, 8, 2, 7, 3, 6, 4, 5]
    assert candidate([0,2,2,2,5,5,-5,-5]) == [-5, 5, -5, 5, 0, 2, 2, 2]
    assert candidate([111111]) == [111111]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(strange_sort_list)