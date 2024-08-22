
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
    # Step 1: Generate the array a
    a = [(i * i - i + 1) for i in range(1, n + 1)]
    
    # Step 2: Count elements in each modulo group
    count = [0, 0, 0]
    
    for number in a:
        count[number % 3] += 1

    result = 0

    # Step 3: Count triples from the same group
    for i in range(3):
        if count[i] >= 3:
            result += comb(count[i], 3)  # n choose 3

    # Step 4: Count one from each group
    result += count[0] * count[1] * count[2]

    return result

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)