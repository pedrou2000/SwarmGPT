
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """


def is_bored(S: str) -> int:
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    >>> is_bored("!I am excited. What is happening? I am curious.")
    1
    """
    # Initialize the boredom counter
    boredom_count = 0
    
    # Split the string into sentences using '.', '?', '!'
    import re
    sentences = re.split(r'(?<=[.?!])\s*', S)
    
    # Iterate through each sentence
    for sentence in sentences:
        # Trim leading and trailing whitespaces
        trimmed_sentence = sentence.strip()
        # Check if the sentence starts with "I"
        if len(trimmed_sentence) > 0 and trimmed_sentence[0] == "I":
            boredom_count += 1
    
    return boredom_count

# Test cases
print(is_bored("Hello world"))  # expected output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # expected output: 1
print(is_bored("!I am excited. What is happening? I am curious."))  # expected output: 1

def check(candidate):

    # Check some simple cases
    assert candidate("Hello world") == 0, "Test 1"
    assert candidate("Is the sky blue?") == 0, "Test 2"
    assert candidate("I love It !") == 1, "Test 3"
    assert candidate("bIt") == 0, "Test 4"
    assert candidate("I feel good today. I will be productive. will kill It") == 2, "Test 5"
    assert candidate("You and I are going for a walk") == 0, "Test 6"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(is_bored)