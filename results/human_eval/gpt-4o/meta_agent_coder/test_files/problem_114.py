
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
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example:
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if not nums:
        return 0  # or raise an exception if an empty array is not considered valid input

    current_min = nums[0]
    global_min = nums[0]

    for num in nums[1:]:
        current_min = min(num, current_min + num)
        global_min = min(global_min, current_min)

    return global_min

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