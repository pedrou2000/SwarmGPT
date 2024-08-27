
def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """


def specialFilter(nums):
    """Write a function that takes an array of numbers as input and returns 
    the number of elements in the array that are greater than 10 and both 
    first and last digits of a number are odd (1, 3, 5, 7, 9).
    For example:
    specialFilter([15, -73, 14, -15]) => 1 
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    
    def is_odd(digit):
        return digit in {'1', '3', '5', '7', '9'}
    
    count = 0
    
    for num in nums:
        if num > 10:  # Check if the number itself is greater than 10
            str_num = str(abs(num))
            first_digit = str_num[0]
            last_digit = str_num[-1]
            
            if is_odd(first_digit) and is_odd(last_digit):
                count += 1
    
    return count

# Example usage:
print(specialFilter([15, -73, 14, -15]))  # Output: 1
print(specialFilter([33, -2, -3, 45, 21, 109]))  # Output: 3

def check(candidate):

    # Check some simple cases
    assert candidate([5, -2, 1, -5]) == 0  
    assert candidate([15, -73, 14, -15]) == 1
    assert candidate([33, -2, -3, 45, 21, 109]) == 2
    assert candidate([43, -12, 93, 125, 121, 109]) == 4
    assert candidate([71, -2, -33, 75, 21, 19]) == 3


    # Check some edge cases that are easy to work out by hand.
    assert candidate([1]) == 0              
    assert candidate([]) == 0                   


check(specialFilter)