
def is_multiply_prime(a):
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """


def is_multiply_prime(a):
    if a < 2:
        return False

    primes = []
    for num in range(2, 100):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            primes.append(num)

    def check_product(primes, remaining, product, count):
        if count == 3:
            return product == a
        for prime in primes:
            if prime > remaining:
                break
            if check_product(primes, remaining // prime, product * prime, count + 1):
                return True
        return False

    return check_product(primes, a, 1, 0)

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