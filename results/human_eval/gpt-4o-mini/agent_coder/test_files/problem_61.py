

def correct_bracketing(brackets: str):
    """ brackets is a string of "(" and ")".
    return True if every opening bracket has a corresponding closing bracket.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """


def correct_bracketing(brackets: str) -> bool:
    counter = 0
    
    for char in brackets:
        if char == '(':
            counter += 1
        elif char == ')':
            counter -= 1
            
        # If counter goes negative, it means there are unmatched closing brackets
        if counter < 0:
            return False
            
    # If counter is zero, all brackets are matched; otherwise, they are not
    return counter == 0



METADATA = {}


def check(candidate):
    assert candidate("()")
    assert candidate("(()())")
    assert candidate("()()(()())()")
    assert candidate("()()((()()())())(()()(()))")
    assert not candidate("((()())))")
    assert not candidate(")(()")
    assert not candidate("(")
    assert not candidate("((((")
    assert not candidate(")")
    assert not candidate("(()")
    assert not candidate("()()(()())())(()")
    assert not candidate("()()(()())()))()")


check(correct_bracketing)