

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """


def is_prime(n):
    """Helper function to check if a number is prime."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_digits(n):
    """Helper function to calculate the sum of digits of a number."""
    return sum(int(digit) for digit in str(n))

def skjkasdkd(lst):
    """Main function to find the largest prime value and return the sum of its digits."""
    primes = [num for num in lst if is_prime(num)]
    if not primes:
        return 0  # In case there are no primes in the list
    largest_prime = max(primes)
    return sum_of_digits(largest_prime)

# Test examples
print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))  # Output: 10
print(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]))  # Output: 25
print(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]))  # Output: 13
print(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]))  # Output: 11
print(skjkasdkd([0,81,12,3,1,21]))  # Output: 3
print(skjkasdkd([0,8,1,2,1,7]))  # Output: 7

def check(candidate):

    # Check some simple cases
    assert candidate([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]) == 10, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]) == 25, "This prints if this assert fails 2 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]) == 13, "This prints if this assert fails 3 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,724,32,71,99,32,6,0,5,91,83,0,5,6]) == 11, "This prints if this assert fails 4 (also good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,81,12,3,1,21]) == 3, "This prints if this assert fails 5 (also good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert candidate([0,8,1,2,1,7]) == 7, "This prints if this assert fails 6 (also good for debugging!)"

    assert candidate([8191]) == 19, "This prints if this assert fails 7 (also good for debugging!)"
    assert candidate([8191, 123456, 127, 7]) == 19, "This prints if this assert fails 8 (also good for debugging!)"
    assert candidate([127, 97, 8192]) == 10, "This prints if this assert fails 9 (also good for debugging!)"

check(skjkasdkd)