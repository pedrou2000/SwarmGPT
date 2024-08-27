
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
        # Generate the array a based on the given formula
        a = [i * i - i + 1 for i in range(1, n + 1)]
        
        # Count the number of elements in a that have a remainder of 0, 1, and 2 when divided by 3
        count_mod = [0, 0, 0]
        for num in a:
            count_mod[num % 3] += 1
        
        # Calculate the number of valid triples
        # We need to choose 3 elements from any combination of remainders such that their sum is a multiple of 3
        count_0 = count_mod[0]
        count_1 = count_mod[1]
        count_2 = count_mod[2]
        
        # (0, 0, 0)
        valid_triples = count_0 * (count_0 - 1) * (count_0 - 2) // 6
        
        # (1, 1, 1)
        valid_triples += count_1 * (count_1 - 1) * (count_1 - 2) // 6
        
        # (2, 2, 2)
        valid_triples += count_2 * (count_2 - 1) * (count_2 - 2) // 6
        
        # (0, 1, 2)
        valid_triples += count_0 * count_1 * count_2
        
        return valid_triples

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)