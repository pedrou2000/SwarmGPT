

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """


    def is_prime(num):
        if num <= 1:
            return False
        if num <= 3:
            return True
        if num % 2 == 0 or num % 3 == 0:
            return False
        i = 5
        while i * i <= num:
            if num % i == 0 or num % (i + 2) == 0:
                return False
            i += 6
        return True

    largest_factor = 1
    # Check for smallest factors first
    while n % 2 == 0:
        largest_factor = 2
        n //= 2
    while n % 3 == 0:
        largest_factor = 3
        n //= 3
    
    # Check for factors starting from 5 and skipping even numbers
    i = 5
    while i * i <= n:
        while n % i == 0:
            largest_factor = i
            n //= i
        while n % (i + 2) == 0:
            largest_factor = i + 2
            n //= (i + 2)
        i += 6
    
    # If n becomes a prime number greater than 4
    if n > 4:
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