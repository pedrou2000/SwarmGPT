

def car_race_collision(n: int):
    """
    Imagine a road that's a perfectly straight infinitely long line.
    n cars are driving left to right;  simultaneously, a different set of n cars
    are driving right to left.   The two sets of cars start out being very far from
    each other.  All cars move in the same speed.  Two cars are said to collide
    when a car that's moving left to right hits a car that's moving right to left.
    However, the cars are infinitely sturdy and strong; as a result, they continue moving
    in their trajectory as if they did not collide.

    This function outputs the number of such collisions.
    """


def car_race_collision(n: int) -> int:
    """ Calculate the number of collisions between cars moving in opposite directions.
    
    Args:
    n (int): The number of cars in each direction.
    
    Returns:
    int: The total number of collisions.
    
    Example:
    >>> car_race_collision(3)
    9
    >>> car_race_collision(0)
    0
    """
    return n * n



METADATA = {}


def check(candidate):
    assert candidate(2) == 4
    assert candidate(3) == 9
    assert candidate(4) == 16
    assert candidate(8) == 64
    assert candidate(10) == 100


check(car_race_collision)