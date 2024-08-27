
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
    # Step 1: Take the absolute value of the number
    num = abs(num)
    
    # Special case for 0
    if num == 0:
        return (1, 0)
    
    # Step 2: Convert the number to a string
    num_str = str(num)
    
    # Step 3: Initialize counters for even and odd digits
    even_count = 0
    odd_count = 0
    
    # Step 4: Loop through each digit in the string representation of the number
    for digit in num_str:
        # Convert the character to an integer
        digit_int = int(digit)
        
        # Check if the digit is even or odd and increment the appropriate counter
        if digit_int % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    
    # Step 5: Return the counts as a tuple
    return (even_count, odd_count)

# Example usage
print(even_odd_count(-12))  # Output: (1, 1)
print(even_odd_count(123))  # Output: (1, 2)
print(even_odd_count(0))    # Output: (1, 0)

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