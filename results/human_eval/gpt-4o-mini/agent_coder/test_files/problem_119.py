
def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '(())()' is good, while the string
    '())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    '''


def match_parens(lst):
    count_open_1 = lst[0].count('(')
    count_close_1 = lst[0].count(')')
    count_open_2 = lst[1].count('(')
    count_close_2 = lst[1].count(')')
    
    # Check first combination: lst[0] + lst[1]
    if (count_open_1 + count_open_2 == count_close_1 + count_close_2):
        if count_open_1 <= count_close_2:
            return 'Yes'
    
    # Check second combination: lst[1] + lst[0]
    if (count_open_2 + count_open_1 == count_close_2 + count_close_1):
        if count_open_2 <= count_close_1:
            return 'Yes'
    
    return 'No'

def check(candidate):

    # Check some simple cases
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    assert candidate(['()', '())']) == 'No'
    assert candidate(['(()(', '()))()']) == 'Yes'
    assert candidate(['((((', '((())']) == 'No'
    assert candidate([')(()', '(()(']) == 'No'
    assert candidate([')(', ')(']) == 'No'
    

    # Check some edge cases that are easy to work out by hand.
    assert candidate(['(', ')']) == 'Yes'
    assert candidate([')', '(']) == 'Yes' 


check(match_parens)