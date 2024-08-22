
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """


def compare_one(a, b):
    def normalize(value):
        if isinstance(value, str):
            # Replace ',' with '.' for decimal point
            value = value.replace(',', '.')
            try:
                return float(value)
            except ValueError:
                return value  # if conversion fails, return the string itself
        return value  # if it's not a string, return it as is

    normalized_a = normalize(a)
    normalized_b = normalize(b)

    if normalized_a == normalized_b:
        return None
    elif normalized_a > normalized_b:
        return a
    else:
        return b

# Example test cases
print(compare_one(1, 2.5))        # ➞ 2.5
print(compare_one(1, "2,3"))      # ➞ "2,3"
print(compare_one("5,1", "6"))    # ➞ "6"
print(compare_one("1", 1))         # ➞ None

def check(candidate):

    # Check some simple cases
    assert candidate(1, 2) == 2
    assert candidate(1, 2.5) == 2.5
    assert candidate(2, 3) == 3
    assert candidate(5, 6) == 6
    assert candidate(1, "2,3") == "2,3"
    assert candidate("5,1", "6") == "6"
    assert candidate("1", "2") == "2"
    assert candidate("1", 1) == None

    # Check some edge cases that are easy to work out by hand.
    assert True


check(compare_one)