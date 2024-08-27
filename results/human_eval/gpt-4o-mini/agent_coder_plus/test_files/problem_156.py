
def int_to_mini_roman(number):
    """
    Given a positive integer, obtain its roman numeral equivalent as a string,
    and return it in lowercase.
    Restrictions: 1 <= num <= 1000

    Examples:
    >>> int_to_mini_roman(19) == 'xix'
    >>> int_to_mini_roman(152) == 'clii'
    >>> int_to_mini_roman(426) == 'cdxxvi'
    """


def int_to_mini_roman(number):
    """ Convert a positive integer to its Roman numeral equivalent in lowercase. """
    roman_numerals = [
        ('m', 1000), ('d', 500), ('c', 100), ('l', 50),
        ('x', 10), ('v', 5), ('i', 1),
        ('cm', 900), ('cd', 400), ('xc', 90), ('xl', 40), ('ix', 9), ('iv', 4)
    ]
    
    result = ""
    
    for roman, value in roman_numerals:
        while number >= value:
            result += roman
            number -= value
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(19) == 'xix'
    assert candidate(152) == 'clii'
    assert candidate(251) == 'ccli'
    assert candidate(426) == 'cdxxvi'
    assert candidate(500) == 'd'
    assert candidate(1) == 'i'
    assert candidate(4) == 'iv'
    assert candidate(43) == 'xliii'
    assert candidate(90) == 'xc'
    assert candidate(94) == 'xciv'
    assert candidate(532) == 'dxxxii'
    assert candidate(900) == 'cm'
    assert candidate(994) == 'cmxciv'
    assert candidate(1000) == 'm'

    # Check some edge cases that are easy to work out by hand.
    assert True


check(int_to_mini_roman)