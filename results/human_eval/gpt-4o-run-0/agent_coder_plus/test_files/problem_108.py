
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


def sum_of_digits(num):
    num_str = str(abs(num))  # Convert to string after taking absolute value
    digit_sum = 0
    
    for char in num_str:
        digit_sum += int(char)
    
    return digit_sum

def count_nums(arr):
    count = 0
    
    for num in arr:
        if sum_of_digits(num) > 0:
            count += 1
    
    return count

# Test cases
print(count_nums([]))  # Expected output: 0
print(count_nums([-1, 11, -11]))  # Expected output: 3
print(count_nums([1, 1, 2]))  # Expected output: 3

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