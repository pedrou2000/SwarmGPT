
def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """


def tri(n):
    if n < 0:
        return []
    
    # Initialize the sequence with the first three values
    sequence = [0, 1, 1]  # tri(0) = 0, tri(1) = 1, tri(2) = 1
    
    # If n is less than 3, return the sequence up to n
    if n < 3:
        return sequence[:n + 1]
    
    for i in range(3, n + 1):
        # tri(n) = tri(n-1) + tri(n-2) + tri(n-3)
        sequence.append(sequence[i - 1] + sequence[i - 2] + sequence[i - 3])
    
    return sequence

# Examples:
print(tri(3))  # Output: [0, 1, 1, 2]
print(tri(0))  # Output: [0]
print(tri(1))  # Output: [0, 1]
print(tri(2))  # Output: [0, 1, 1]
print(tri(4))  # Output: [0, 1, 1, 2, 4]
print(tri(-1)) # Output: []

# Additional tests
print(tri(5))  # Output: [0, 1, 1, 2, 4, 7]
print(tri(6))  # Output: [0, 1, 1, 2, 4, 7, 13]
print(tri(10)) # Output: [0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149]

def check(candidate):

    # Check some simple cases
    
    assert candidate(3) == [1, 3, 2.0, 8.0]
    assert candidate(4) == [1, 3, 2.0, 8.0, 3.0]
    assert candidate(5) == [1, 3, 2.0, 8.0, 3.0, 15.0]
    assert candidate(6) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0]
    assert candidate(7) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0]
    assert candidate(8) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0]
    assert candidate(9) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0]
    assert candidate(20) == [1, 3, 2.0, 8.0, 3.0, 15.0, 4.0, 24.0, 5.0, 35.0, 6.0, 48.0, 7.0, 63.0, 8.0, 80.0, 9.0, 99.0, 10.0, 120.0, 11.0]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(0) == [1]
    assert candidate(1) == [1, 3]

check(tri)