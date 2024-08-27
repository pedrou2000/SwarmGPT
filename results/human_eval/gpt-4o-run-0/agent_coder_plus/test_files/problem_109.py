
def move_one_ball(arr):
    """We have an array 'arr' of N integers arr[1], arr[2], ..., arr[N].The
    numbers in the array will be randomly ordered. Your task is to determine if
    it is possible to get an array sorted in non-decreasing order by performing 
    the following operation on the given array:
        You are allowed to perform right shift operation any number of times.
    
    One right shift operation means shifting all elements of the array by one
    position in the right direction. The last element of the array will be moved to
    the starting position in the array i.e. 0th index. 

    If it is possible to obtain the sorted array by performing the above operation
    then return True else return False.
    If the given array is empty then return True.

    Note: The given list is guaranteed to have unique elements.

    For Example:
    
    move_one_ball([3, 4, 5, 1, 2])==>True
    Explanation: By performin 2 right shift operations, non-decreasing order can
                 be achieved for the given array.
    move_one_ball([3, 5, 4, 1, 2])==>False
    Explanation:It is not possible to get non-decreasing order for the given
                array by performing any number of right shift operations.
                
    """


def move_one_ball(arr):
    if not arr:  # Check for empty array
        return True

    n = len(arr)
    
    # Function to check if the array is sorted in non-decreasing order
    def is_sorted(array):
        for i in range(1, len(array)):
            if array[i] < array[i - 1]:
                return False
        return True

    # Generate all possible right shifts and check if any is sorted
    for i in range(n):
        # Perform right shift
        shifted_arr = arr[-i:] + arr[:-i]
        if is_sorted(shifted_arr):
            return True

    return False

# Test cases
print(move_one_ball([3, 4, 5, 1, 2]))  # Should return True
print(move_one_ball([3, 5, 4, 1, 2]))  # Should return False

def check(candidate):

    # Check some simple cases
    assert candidate([3, 4, 5, 1, 2])==True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([3, 5, 10, 1, 2])==True
    assert candidate([4, 3, 1, 2])==False
    # Check some edge cases that are easy to work out by hand.
    assert candidate([3, 5, 4, 1, 2])==False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([])==True

check(move_one_ball)