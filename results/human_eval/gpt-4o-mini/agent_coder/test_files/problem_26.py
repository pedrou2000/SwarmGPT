from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """


from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = {}
    
    # Count occurrences of each number
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    # Filter and create the result list
    result = []
    for number in numbers:
        if counts[number] == 1:
            result.append(number)

    return result



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate([]) == []
    assert candidate([1, 2, 3, 4]) == [1, 2, 3, 4]
    assert candidate([1, 2, 3, 2, 4, 3, 5]) == [1, 4, 5]

check(remove_duplicates)