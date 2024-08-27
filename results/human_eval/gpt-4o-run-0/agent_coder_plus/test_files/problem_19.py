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
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    
    # Mapping of string numbers to their respective integer values
    number_to_int = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3,
        'four': 4, 'five': 5, 'six': 6, 'seven': 7,
        'eight': 8, 'nine': 9
    }
    
    # Split the input string into individual number words
    number_words = numbers.split()
    
    # Convert number words to their integer equivalents
    number_ints = [number_to_int[word] for word in number_words]
    
    # Sort the integers
    sorted_ints = sorted(number_ints)
    
    # Reverse mapping from integer values to string numbers
    int_to_number = {v: k for k, v in number_to_int.items()}
    
    # Convert sorted integers back to their string representations
    sorted_number_words = [int_to_number[num] for num in sorted_ints]
    
    # Join the sorted number words into a single string
    sorted_numbers_str = ' '.join(sorted_number_words)
    
    return sorted_numbers_str

# Example usage
print(sort_numbers('three one five'))  # Output: 'one three five'



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