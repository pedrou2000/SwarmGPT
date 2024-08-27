

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """


def largest_prime_factor(n: int) -> int:
    largest_factor = 1
    
    # Check for factor 2
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    
    # Check for odd factors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            largest_factor = i
            n //= i
            
    # If n is still greater than 1, then n itself is prime
    if n > 1:
        largest_factor = n
        
    return largest_factor



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)