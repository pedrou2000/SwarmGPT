
def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """


def even_odd_count(num):
    """Given an integer, return a tuple that has the number of even and odd digits respectively.

    Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """
    num = abs(num)  # Step 1: Handle negative numbers
    num_str = str(num)  # Step 2: Convert to string
    even_count = 0  # Step 3: Initialize even counter
    odd_count = 0   # Step 3: Initialize odd counter

    for char in num_str:  # Step 4: Iterate through the string
        digit = int(char)  # Convert character back to integer
        if digit % 2 == 0:  # Check if digit is even
            even_count += 1  # Increment even counter
        else:  # Otherwise, it's odd
            odd_count += 1   # Increment odd counter

    return (even_count, odd_count)  # Step 5: Return the counts as a tuple

def check(candidate):

    # Check some simple cases
    assert candidate(7) == (0, 1)
    assert candidate(-78) == (1, 1)
    assert candidate(3452) == (2, 2)
    assert candidate(346211) == (3, 3)
    assert candidate(-345821) == (3, 3)
    assert candidate(-2) == (1, 0)
    assert candidate(-45347) == (2, 3)
    assert candidate(0) == (1, 0)


    # Check some edge cases that are easy to work out by hand.
    assert True


check(even_odd_count)