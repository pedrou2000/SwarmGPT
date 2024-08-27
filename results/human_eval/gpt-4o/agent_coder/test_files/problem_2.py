

def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """


from decimal import Decimal, getcontext

def truncate_number(number: float) -> float:
    """
    Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
    # Set the precision for decimal operations
    getcontext().prec = 10  # You can adjust the precision as needed
    
    decimal_number = Decimal(str(number))
    integer_part = int(decimal_number)
    decimal_part = decimal_number - Decimal(integer_part)
    
    return float(decimal_part)

# Test cases
print(truncate_number(3.5))          # Expected: 0.5
print(truncate_number(5.89))         # Expected: 0.89
print(truncate_number(0.45))         # Expected: 0.45
print(truncate_number(4.0))          # Expected: 0.0
print(truncate_number(12345.9999))   # Expected: 0.9999
print(truncate_number(987654321.6789))  # Expected: 0.6789
print(truncate_number(0))            # Expected: 0.0



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6

check(truncate_number)