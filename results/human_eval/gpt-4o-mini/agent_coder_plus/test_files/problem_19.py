from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """


from typing import List

def sort_numbers(numbers: str) -> str:
    number_map = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # Inverting the dictionary for easy reverse lookup
    reverse_map = {v: k for k, v in number_map.items()}
    
    # Split the input string into words
    words = numbers.split()
    
    # Convert words to numbers
    number_list = [number_map[word] for word in words]
    
    # Sort the numbers
    number_list.sort()
    
    # Convert numbers back to words
    sorted_words = [reverse_map[number] for number in number_list]
    
    # Join the sorted words into a single string
    return ' '.join(sorted_words)

# Example usage:
# print(sort_numbers('three one five'))  # Output: 'one three five'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == ''
    assert candidate('three') == 'three'
    assert candidate('three five nine') == 'three five nine'
    assert candidate('five zero four seven nine eight') == 'zero four five seven eight nine'
    assert candidate('six five four three two one zero') == 'zero one two three four five six'

check(sort_numbers)