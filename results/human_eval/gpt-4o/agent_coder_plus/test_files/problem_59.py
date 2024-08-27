

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """


def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    largest_factor = 1
    
    # Step 1: Remove all factors of 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Step 2: Remove factors of odd numbers from 3 upwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            largest_factor = factor
            n //= factor
        factor += 2
    
    # Step 3: If n is still greater than 2, then it is prime
    if n > 2:
        largest_factor = n
    
    return largest_factor

# Example usage
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)