
def count_nums(arr):
    """
    Write a function count_nums which takes an array of integers and returns
    the number of elements which has a sum of digits > 0.
    If a number is negative, then its first signed digit will be negative:
    e.g. -123 has signed digits -1, 2, and 3.
    >>> count_nums([]) == 0
    >>> count_nums([-1, 11, -11]) == 1
    >>> count_nums([1, 1, 2]) == 3
    """


def count_nums(arr):
    count = 0
    
    for number in arr:
        sum_digits = 0
        str_number = str(number)
        
        for idx, char in enumerate(str_number):
            if idx == 0 and char == '-':
                # If the first character is '-', we add its negative value
                sum_digits += -int(str_number[1]) if len(str_number) > 1 else 0
            elif char.isdigit():
                # For all other digits, we add their positive value
                sum_digits += int(char)
        
        if sum_digits > 0:
            count += 1
            
    return count

def check(candidate):

    # Check some simple cases
    assert candidate([]) == 0
    assert candidate([-1, -2, 0]) == 0
    assert candidate([1, 1, 2, -2, 3, 4, 5]) == 6
    assert candidate([1, 6, 9, -6, 0, 1, 5]) == 5
    assert candidate([1, 100, 98, -7, 1, -1]) == 4
    assert candidate([12, 23, 34, -45, -56, 0]) == 5
    assert candidate([-0, 1**0]) == 1
    assert candidate([1]) == 1

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(count_nums)