from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """


from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Edge case handling
    if not isinstance(string, str):
        raise ValueError("Input must be a string")
    
    # Efficient list comprehension approach
    return [string[:i] for i in range(1, len(string) + 1)]

# Tests
assert all_prefixes('abc') == ['a', 'ab', 'abc'], "Basic test with small string"
assert all_prefixes('a') == ['a'], "Test with a single character string"
assert all_prefixes('') == [], "Test with an empty string"
assert all_prefixes('ab') == ['a', 'ab'], "Test with two characters string"
assert all_prefixes('abcdef') == ['a', 'ab', 'abc', 'abcd', 'abcde', 'abcdef'], "Test with longer string"
assert all_prefixes('123') == ['1', '12', '123'], "Test with numeric characters"
assert all_prefixes('aBcD') == ['a', 'aB', 'aBc', 'aBcD'], "Test with mixed case string"

print("All tests passed.")



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']

check(all_prefixes)