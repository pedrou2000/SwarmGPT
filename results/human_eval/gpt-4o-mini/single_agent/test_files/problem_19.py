from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """


    # Mapping of words to their corresponding numeric values
    word_to_number = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }
    
    # Split the input string into words
    words = numbers.split()
    
    # Convert words to their numeric values
    numeric_values = [word_to_number[word] for word in words]
    
    # Sort the numeric values
    sorted_numbers = sorted(numeric_values)
    
    # Convert back to words
    number_to_word = {v: k for k, v in word_to_number.items()}
    sorted_words = [number_to_word[num] for num in sorted_numbers]
    
    # Join the sorted words into a string and return
    return ' '.join(sorted_words)



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