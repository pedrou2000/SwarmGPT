
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """


def make_a_pile(n):
    """ Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is simply the current level's stone count plus two.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    
    >>> make_a_pile(3)
    [3, 5, 7]
    >>> make_a_pile(4)
    [4, 6, 8, 10]
    >>> make_a_pile(5)
    [5, 7, 9, 11, 13]
    >>> make_a_pile(1)
    [1]
    >>> make_a_pile(2)
    [2, 4]
    >>> make_a_pile(0)
    []
    """
    result = []
    current_stones = n
    
    for i in range(n):
        result.append(current_stones)
        current_stones += 2  # Increment by 2 for the next level
    
    return result

def check(candidate):

    # Check some simple cases
    assert candidate(3) == [3, 5, 7], "Test 3"
    assert candidate(4) == [4,6,8,10], "Test 4"
    assert candidate(5) == [5, 7, 9, 11, 13]
    assert candidate(6) == [6, 8, 10, 12, 14, 16]
    assert candidate(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(make_a_pile)