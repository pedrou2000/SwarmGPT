
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


def get_max_triples(n):
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Count the elements in a modulo 3
    count_mod = [0, 0, 0]
    for num in a:
        count_mod[num % 3] += 1
    
    # Calculate the number of valid triples
    # We need to find C(count_mod[i], 3) + C(count_mod[i], 1) * C(count_mod[j], 1) * C(count_mod[k], 1)
    # for all combinations of i, j, k such that (i + j + k) % 3 == 0
    def comb(n, k):
        if n < k:
            return 0
        if k == 2:
            return n * (n - 1) // 2
        if k == 3:
            return n * (n - 1) * (n - 2) // 6
        return 0
    
    result = 0
    # (0,0,0), (1,1,1), (2,2,2)
    result += comb(count_mod[0], 3)
    result += comb(count_mod[1], 3)
    result += comb(count_mod[2], 3)
    # (0,1,2)
    result += count_mod[0] * count_mod[1] * count_mod[2]
    
    return result

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)