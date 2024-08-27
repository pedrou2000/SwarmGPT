
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
        open_count1 = lst[0].count('(')
        close_count1 = lst[0].count(')')
        open_count2 = lst[1].count('(')
        close_count2 = lst[1].count(')')
        
        # Check the two possible concatenations
        # 1. First string followed by second string
        if open_count1 + open_count2 == close_count1 + close_count2:
            if open_count1 <= close_count2 + open_count2:
                return 'Yes'
        
        # 2. Second string followed by first string
        if open_count2 + open_count1 == close_count2 + close_count1:
            if open_count2 <= close_count1 + open_count1:
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