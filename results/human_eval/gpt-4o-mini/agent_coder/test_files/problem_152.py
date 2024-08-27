
def compare(game,guess):
    """I think we all remember that feeling when the result of some long-awaited
    event is finally known. The feelings and thoughts you have at that moment are
    definitely worth noting down and comparing.
    Your task is to determine if a person correctly guessed the results of a number of matches.
    You are given two arrays of scores and guesses of equal length, where each index shows a match. 
    Return an array of the same length denoting how far off each guess was. If they have guessed correctly,
    the value is 0, and if not, the value is the absolute difference between the guess and the score.
    
    
    example:

    compare([1,2,3,4,5,1],[1,2,3,4,2,-2]) -> [0,0,0,0,3,3]
    compare([0,5,0,0,0,4],[4,1,1,0,0,-2]) -> [4,4,1,0,0,6]
    """


from typing import List

def compare(game: List[int], guess: List[int]) -> List[int]:
    """Compares the actual game scores with the guessed scores.
    
    Args:
    game: List of actual scores.
    guess: List of guessed scores.
    
    Returns:
    A list of absolute differences or zeroes.
    
    >>> compare([1,2,3,4,5,1],[1,2,3,4,2,-2])
    [0, 0, 0, 0, 3, 3]
    >>> compare([0,5,0,0,0,4],[4,1,1,0,0,-2])
    [4, 4, 1, 0, 0, 6]
    """
    result = []
    for i in range(len(game)):
        if guess[i] == game[i]:
            result.append(0)
        else:
            result.append(abs(guess[i] - game[i]))
    return result

def check(candidate):

    # Check some simple cases
    assert candidate([1,2,3,4,5,1],[1,2,3,4,2,-2])==[0,0,0,0,3,3], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([0,0,0,0,0,0],[0,0,0,0,0,0])==[0,0,0,0,0,0], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3],[-1,-2,-3])==[2,4,6], "This prints if this assert fails 1 (good for debugging!)"
    assert candidate([1,2,3,5],[-1,2,3,4])==[2,0,0,1], "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(compare)