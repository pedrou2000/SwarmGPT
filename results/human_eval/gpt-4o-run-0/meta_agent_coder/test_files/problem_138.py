
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """


def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is less than the smallest sum of four positive even numbers
    if n < 8:
        return False
    
    # Check if n is even
    if n % 2 == 0:
        return True
    
    return False

# Test cases
print(is_equal_to_sum_even(4))  # Expected output: False
print(is_equal_to_sum_even(6))  # Expected output: False
print(is_equal_to_sum_even(8))  # Expected output: True
print(is_equal_to_sum_even(10)) # Expected output: True
print(is_equal_to_sum_even(14)) # Expected output: True
print(is_equal_to_sum_even(15)) # Expected output: False

def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True

check(is_equal_to_sum_even)