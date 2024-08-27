
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
    result = []
    lst_copy = lst[:]  # Make a copy of the list
    pick_min = True  # Flag to indicate whether to pick min or max

    while lst_copy:
        if pick_min:
            value = min(lst_copy)
        else:
            value = max(lst_copy)
        lst_copy.remove(value)
        result.append(value)
        pick_min = not pick_min  # Switch between min and max

    return result

# Test cases to verify the implementation
assert strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3], "Test Case 1 Failed"
assert strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5], "Test Case 2 Failed"
assert strange_sort_list([]) == [], "Test Case 3 Failed"
assert strange_sort_list([10, 1, 20, 2, 30, 3]) == [1, 30, 2, 20, 3, 10], "Test Case 4 Failed"
assert strange_sort_list([1, 2]) == [1, 2], "Test Case 5 Failed"
assert strange_sort_list([2, 1]) == [1, 2], "Test Case 6 Failed"
assert strange_sort_list([3, 1, 2]) == [1, 3, 2], "Test Case 7 Failed"
assert strange_sort_list([3, 3, 2, 1, 1]) == [1, 3, 1, 3, 2], "Test Case 8 Failed"

print("All test cases pass")

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