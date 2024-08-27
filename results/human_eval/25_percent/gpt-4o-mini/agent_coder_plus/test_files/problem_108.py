
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
    
    for num in arr:
        # Convert number to string to process each digit
        str_num = str(num)
        sum_of_digits = 0
        
        for i, char in enumerate(str_num):
            if char == '-':
                # Skip the '-' sign
                continue
            digit = int(char)
            if i == 1 and str_num[0] == '-':  # First digit of a negative number
                sum_of_digits -= digit
            else:
                sum_of_digits += digit
        
        if sum_of_digits > 0:
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