
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
    # Step 1: Create the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Step 2: Count remainders
    count = [0, 0, 0]  # count for remainders 0, 1, 2
    for num in a:
        count[num % 3] += 1

    # Step 3: Calculate the number of valid triples
    total_triples = 0
    
    # Case 1: All three from the same remainder group
    for c in count:
        if c >= 3:
            total_triples += (c * (c - 1) * (c - 2)) // 6  # nC3

    # Case 2: One from each group (0, 1, 2)
    total_triples += count[0] * count[1] * count[2]

    return total_triples

# Test the function with the specific case that failed
print(get_max_triples(3))  # This should match the expected result for Test Case 3

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)