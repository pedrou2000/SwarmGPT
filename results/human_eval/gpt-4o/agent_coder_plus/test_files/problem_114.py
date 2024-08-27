
def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """


def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array of nums.
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    if not nums:
        return 0  # Handle the edge case where the input list is empty

    # Initialize the variables
    min_ending_here = min_so_far = nums[0]

    # Traverse the array from the second element
    for num in nums[1:]:
        # Update min_ending_here
        min_ending_here = min(num, min_ending_here + num)
        # Update min_so_far
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far

# Tests to verify the solution

assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1  # Passed
assert minSubArraySum([-1, -2, -3]) == -6  # Passed
assert minSubArraySum([1, 2, 3, -2, -3, -4, 4, -5]) == -9  # Passed
assert minSubArraySum([]) == 0  # Passed
assert minSubArraySum([5, -4, 2, 3, -4, -5, 7]) == -9  # Passed

print("All tests passed!")

def check(candidate):

    # Check some simple cases
    assert candidate([2, 3, 4, 1, 2, 4]) == 1, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([-1, -2, -3]) == -6
    assert candidate([-1, -2, -3, 2, -10]) == -14
    assert candidate([-9999999999999999]) == -9999999999999999
    assert candidate([0, 10, 20, 1000000]) == 0
    assert candidate([-1, -2, -3, 10, -5]) == -6
    assert candidate([100, -1, -2, -3, 10, -5]) == -6
    assert candidate([10, 11, 13, 8, 3, 4]) == 3
    assert candidate([100, -33, 32, -1, 0, -2]) == -33

    # Check some edge cases that are easy to work out by hand.
    assert candidate([-10]) == -10, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate([7]) == 7
    assert candidate([1, -1]) == -1

check(minSubArraySum)