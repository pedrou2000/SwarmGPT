
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """


from itertools import combinations

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(limit):
    """Generate all prime numbers less than a given limit."""
    primes = []
    for num in range(2, limit):
        if is_prime(num):
            primes.append(num)
    return primes

def is_multiply_prime(a):
    """Check if the given number is the multiplication of 3 prime numbers."""
    if a >= 100:
        return False
    
    primes = generate_primes(100)
    
    for combo in combinations(primes, 3):
        if combo[0] * combo[1] * combo[2] == a:
            return True
    
    return False

# Test cases
print(is_multiply_prime(30)) # True, because 30 = 2 * 3 * 5
print(is_multiply_prime(60)) # False, because 60 = 2 * 2 * 3 * 5
print(is_multiply_prime(105)) # True, because 105 = 3 * 5 * 7
print(is_multiply_prime(100)) # False, because it is greater than 100

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