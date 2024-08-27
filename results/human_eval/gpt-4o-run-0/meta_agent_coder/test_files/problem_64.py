
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """


def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    # Convert the string to lowercase
    s = s.lower()
    
    # Define the set of vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Initialize count
    count = 0
    
    # Iterate through the string
    for i, char in enumerate(s):
        if char in vowels:
            count += 1
        # Check if 'y' is the last character
        elif char == 'y' and i == len(s) - 1:
            count += 1
    
    return count

# Adding more test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Additional test cases
    assert vowels_count("hello") == 2
    assert vowels_count("yesterday") == 3
    assert vowels_count("PYTHON") == 1
    assert vowels_count("sky") == 1
    assert vowels_count("xyz") == 0
    assert vowels_count("rhythm") == 0

def check(candidate):

    # Check some simple cases
    assert candidate("abcde") == 2, "Test 1"
    assert candidate("Alone") == 3, "Test 2"
    assert candidate("key") == 2, "Test 3"
    assert candidate("bye") == 1, "Test 4"
    assert candidate("keY") == 2, "Test 5"
    assert candidate("bYe") == 1, "Test 6"
    assert candidate("ACEDY") == 3, "Test 7"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(vowels_count)