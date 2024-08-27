
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
    s = s.lower()  # Convert to lowercase
    count = 0
    
    for index, char in enumerate(s):
        if char in 'aeiou':
            count += 1
        if char == 'y' and index == len(s) - 1:
            count += 1
    
    return count

# Additional test cases
print(vowels_count(""))  # 0
print(vowels_count("bcdfg"))  # 0
print(vowels_count("a"))  # 1
print(vowels_count("abcdefghij"))  # 3
print(vowels_count("hello"))  # 2
print(vowels_count("sky"))  # 1
print(vowels_count("rhythm"))  # 0
print(vowels_count("y"))  # 1
print(vowels_count("yay"))  # 1
print(vowels_count("YAY"))  # 1
print(vowels_count("syzygy"))  # 1

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