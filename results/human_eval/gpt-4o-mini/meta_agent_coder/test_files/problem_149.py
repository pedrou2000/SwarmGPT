
def sorted_list_sum(lst):
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    assert list_sort(["aa", "a", "aaa"]) => ["aa"]
    assert list_sort(["ab", "a", "aaa", "cd"]) => ["ab", "cd"]
    """


from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """Filter out strings with odd lengths and return the sorted list of remaining strings.
    
    >>> sorted_list_sum(["aa", "a", "aaa"])
    ['aa']
    >>> sorted_list_sum(["ab", "a", "aaa", "cd"])
    ['ab', 'cd']
    """
    # Step 1: Filter out odd length strings
    filtered_list = [s for s in lst if len(s) % 2 == 0]
    
    # Step 2: Sort the filtered list first by length, then alphabetically
    filtered_list.sort(key=lambda x: (len(x), x))
    
    # Step 3: Return the sorted list
    return filtered_list

def check(candidate):

    # Check some simple cases
    assert candidate(["aa", "a", "aaa"]) == ["aa"]
    assert candidate(["school", "AI", "asdf", "b"]) == ["AI", "asdf", "school"]
    assert candidate(["d", "b", "c", "a"]) == []
    assert candidate(["d", "dcba", "abcd", "a"]) == ["abcd", "dcba"]

    # Check some edge cases that are easy to work out by hand.
    assert candidate(["AI", "ai", "au"]) == ["AI", "ai", "au"]
    assert candidate(["a", "b", "b", "c", "c", "a"]) == []
    assert candidate(['aaaa', 'bbbb', 'dd', 'cc']) == ["cc", "dd", "aaaa", "bbbb"]


check(sorted_list_sum)