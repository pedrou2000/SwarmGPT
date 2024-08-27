
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
    if n < 3:
        return 0
    
    # Step 1: Generate the array a
    a = [i * i - i + 1 for i in range(1, n + 1)]
    
    # Step 2: Initialize the counter for valid triples
    count = 0
    
    # Frequency array to count occurrences of elements modulo 3
    freq = [0] * 3
    for value in a:
        freq[value % 3] += 1
    
    # Step 3: Calculate valid triples
    # Triples (0, 0, 0)
    count += (freq[0] * (freq[0] - 1) * (freq[0] - 2)) // 6
    
    # Triples (1, 1, 1)
    count += (freq[1] * (freq[1] - 1) * (freq[1] - 2)) // 6
    
    # Triples (2, 2, 2)
    count += (freq[2] * (freq[2] - 1) * (freq[2] - 2)) // 6
    
    # Triples (0, 1, 2)
    count += freq[0] * freq[1] * freq[2]
    
    # Step 4: Return the count of valid triples
    return count

# Example usage:
print(get_max_triples(5))  # Example case
print(get_max_triples(0))  # Edge case with n = 0
print(get_max_triples(2))  # Edge case with n = 2
print(get_max_triples(6))  # Larger array length 6
print(get_max_triples(10)) # Larger array length 10

def check(candidate):

    assert candidate(5) == 1
    assert candidate(6) == 4
    assert candidate(10) == 36
    assert candidate(100) == 53361

check(get_max_triples)