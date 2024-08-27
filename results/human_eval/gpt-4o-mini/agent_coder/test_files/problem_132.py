
def is_nested(string):
    '''
    Create a function that takes a string as input which contains only square brackets.
    The function should return True if and only if there is a valid subsequence of brackets 
    where at least one bracket in the subsequence is nested.

    is_nested('[[]]') ➞ True
    is_nested('[]]]]]]][[[[[]') ➞ False
    is_nested('[][]') ➞ False
    is_nested('[]') ➞ False
    is_nested('[[][]]') ➞ True
    is_nested('[[]][[') ➞ True
    '''


def is_nested(string):
    open_count = 0
    has_nested = False

    for char in string:
        if char == '[':
            open_count += 1
            # If we encounter a second opening bracket, we know we have nesting
            if open_count >= 2:
                has_nested = True
        elif char == ']':
            # If we encounter a closing bracket but no opening bracket, return False immediately
            if open_count == 0:
                return False
            open_count -= 1

    # The string is valid if all open brackets are closed and there is nesting
    return open_count == 0 and has_nested

# Test cases
print(is_nested('[[]]'))            # True
print(is_nested('[]]]]]]][[[[[]'))   # False
print(is_nested('[][]'))            # False
print(is_nested('[]'))              # False
print(is_nested('[[][]]'))          # True
print(is_nested('[[]][['))          # True
print(is_nested('[[[]]]'))          # True
print(is_nested('[][[[]]][]'))      # True
print(is_nested('['))                # False
print(is_nested(']'))                # False
print(is_nested(''))                 # False

def check(candidate):

    # Check some simple cases
    assert candidate('[[]]') == True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate('[]]]]]]][[[[[]') == False
    assert candidate('[][]') == False
    assert candidate(('[]')) == False
    assert candidate('[[[[]]]]') == True
    assert candidate('[]]]]]]]]]]') == False
    assert candidate('[][][[]]') == True
    assert candidate('[[]') == False
    assert candidate('[]]') == False
    assert candidate('[[]][[') == True
    assert candidate('[[][]]') == True

    # Check some edge cases that are easy to work out by hand.
    assert candidate('') == False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate('[[[[[[[[') == False
    assert candidate(']]]]]]]]') == False


check(is_nested)