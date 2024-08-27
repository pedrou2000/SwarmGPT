

def triangle_area(a, h):
    """Given length of a side and high return area for a triangle.
    >>> triangle_area(5, 3)
    7.5
    """


def triangle_area(a: float, h: float) -> float:
    """Given length of a side and height, return the area of a triangle.
    >>> triangle_area(5, 3)
    7.5
    """
    # Calculate the area using the formula: (1/2) * base * height
    area = 0.5 * a * h
    return area



METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)