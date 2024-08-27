
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
        def to_float(value):
            if isinstance(value, str):
                value = value.replace(",", ".")
                return float(value)
            return float(value)
        
        if a == b:
            return None
        
        # Compare in original types if different types
        if type(a) != type(b):
            float_a = to_float(a)
            float_b = to_float(b)
            return a if float_a > float_b else b
        
        # Compare in native types if same type
        return a if a > b else b

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