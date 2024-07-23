
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
    count = 0
    
    # Count occurrences of a[i] % 3
    mod_count = [0] * 3
    for value in a:
        mod_count[value % 3] += 1

    # Calculate the number of valid triples
    # Case 1: all three numbers have the same remainder
    for m in mod_count:
        if m >= 3:
            count += (m * (m - 1) * (m - 2)) // 6

    # Case 2: one number from each remainder group
    count += mod_count[0] * mod_count[1] * mod_count[2]
    
    return count

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)