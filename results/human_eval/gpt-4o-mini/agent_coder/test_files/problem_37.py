

def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """


def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Step 1: Extract even-indexed elements
    even_elements = [l[i] for i in range(len(l)) if i % 2 == 0]

    # Step 2: Sort even-indexed elements
    even_elements.sort()

    # Step 3: Reconstruct the list
    result = l[:]  # Start with a copy of the original list
    j = 0  # Pointer for even_elements
    for i in range(len(l)):
        if i % 2 == 0:  # If the index is even
            result[i] = even_elements[j]
            j += 1  # Move to the next even element

    return result



METADATA = {}


def check(candidate):
    assert tuple(candidate([1, 2, 3])) == tuple([1, 2, 3])
    assert tuple(candidate([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) == tuple([-10, 3, -5, 2, -3, 3, 5, 0, 9, 1, 123])
    assert tuple(candidate([5, 8, -12, 4, 23, 2, 3, 11, 12, -10])) == tuple([-12, 8, 3, 4, 5, 2, 12, 11, 23, -10])


check(sort_even)