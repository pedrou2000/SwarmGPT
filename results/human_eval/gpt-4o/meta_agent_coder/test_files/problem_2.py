

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
    """ Given a positive floating point number, it can be decomposed into
    an integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).
    
    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10.75)
    0.75
    >>> truncate_number(5.0)
    0.0
    """
    # Set the precision for Decimal
    getcontext().prec = 18
    
    decimal_number = Decimal(str(number))
    integer_part = int(decimal_number)
    decimal_part = decimal_number - Decimal(integer_part)
    return float(decimal_part)

# Test cases
print(truncate_number(5.999))          # Expected output: 0.999
print(truncate_number(999999.999999))  # Expected output: 0.999999
print(truncate_number(1.0000001))      # Expected output: 0.0000001
print(truncate_number(10000000000.1))  # Expected output: 0.1



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate(3.5) == 0.5
    assert abs(candidate(1.33) - 0.33) < 1e-6
    assert abs(candidate(123.456) - 0.456) < 1e-6

check(truncate_number)