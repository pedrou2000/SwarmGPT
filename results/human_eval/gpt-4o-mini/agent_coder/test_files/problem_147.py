
def get_max_triples(n):
    """
    You are given a positive integer n. You have to create an integer array a of length n.
        For each i (1 ≤ i ≤ n), the value of a[i] = i * i - i + 1.
        Return the number of triples (a[i], a[j], a[k]) of a where i < j < k, 
    and a[i] + a[j] + a[k] is a multiple of 3.

    Example :
        Input: n = 5
        Output: 1
        Explanation: 
        a = [1, 3, 7, 13, 21]
        The only valid triple is (1, 7, 13).
    """


from math import comb

def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    count_0 = count_1 = count_2 = 0

    for value in a:
        if value % 3 == 0:
            count_0 += 1
        elif value % 3 == 1:
            count_1 += 1
        else:
            count_2 += 1

    result = 0
    
    # Calculate combinations
    if count_0 >= 3:
        result += comb(count_0, 3)
    if count_1 >= 3:
        result += comb(count_1, 3)
    if count_2 >= 3:
        result += comb(count_2, 3)
    
    # Count one from each category
    result += count_0 * count_1 * count_2

    return result

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)