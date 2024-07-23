
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
        # Count the number of open and close parentheses in both strings
        open1, close1 = lst[0].count('('), lst[0].count(')')
        open2, close2 = lst[1].count('('), lst[1].count(')')
        
        # Check both concatenation orders
        # Order 1: lst[0] + lst[1]
        # Order 2: lst[1] + lst[0]
        
        # Check if lst[0] + lst[1] can be balanced
        if open1 + open2 >= close1 + close2 and open1 >= close2:
            return 'Yes'
        
        # Check if lst[1] + lst[0] can be balanced
        if open2 + open1 >= close2 + close1 and open2 >= close1:
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