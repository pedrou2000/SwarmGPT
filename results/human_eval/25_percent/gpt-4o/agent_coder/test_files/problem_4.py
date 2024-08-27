from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """


from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """ For a given list of input numbers, calculate Mean Absolute Deviation
    around the mean of this dataset.
    Mean Absolute Deviation is the average absolute difference between each
    element and a centerpoint (mean in this case):
    MAD = average | x - x_mean |
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    # Step 1: Calculate the mean of the numbers
    mean = sum(numbers) / len(numbers)
    
    # Step 2: Initialize a variable to store the sum of absolute deviations
    sum_absolute_deviation = 0
    
    # Step 3: Loop through each number to calculate absolute deviation
    for number in numbers:
        sum_absolute_deviation += abs(number - mean)
    
    # Step 4: Calculate the mean of these absolute deviations
    mad = sum_absolute_deviation / len(numbers)
    
    # Step 5: Return the mean absolute deviation
    return mad

# Test the function
print(mean_absolute_deviation([1.0, 2.0, 3.0, 4.0]))  # Output should be 1.0



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert abs(candidate([1.0, 2.0, 3.0]) - 2.0/3.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0]) - 1.0) < 1e-6
    assert abs(candidate([1.0, 2.0, 3.0, 4.0, 5.0]) - 6.0/5.0) < 1e-6


check(mean_absolute_deviation)