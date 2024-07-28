
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """


def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate a list of prime numbers less than the given limit."""
    return [num for num in range(2, limit) if is_prime(num)]

def is_multiply_prime(a):
    """Returns true if the given number is the multiplication of 3 prime numbers."""
    if a < 2:
        return False  # No product of three primes can be less than 2
    
    primes = generate_primes(100)
    
    # Iterate over all combinations of primes with repetitions
    for i in range(len(primes)):
        for j in range(len(primes)):
            for k in range(len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
                    return True
                    
    return False

# Example test cases
print(is_multiply_prime(60))  # Expected: True (2 * 3 * 5)
print(is_multiply_prime(15))  # Expected: False
print(is_multiply_prime(42))  # Expected: True (2 * 3 * 7)
print(is_multiply_prime(77))  # Expected: False
print(is_multiply_prime(33))  # Expected: False
print(is_multiply_prime(72))  # Expected: False

def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


check(is_multiply_prime)