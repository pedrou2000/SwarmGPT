
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
    import re  # Importing regular expressions module

    # Split the string on '.', '?', '!'
    sentences = re.split(r'[.?!]', S)
    
    boredom_count = 0
    
    # Iterate through each sentence
    for sentence in sentences:
        # Strip leading and trailing whitespace
        trimmed_sentence = sentence.strip()
        # Check if the sentence starts with "I"
        if trimmed_sentence.startswith("I "):
            boredom_count += 1
    
    return boredom_count

# Example usage:
print(is_bored("Hello world"))  # Output: 0
print(is_bored("The sky is blue. The sun is shining. I love this weather"))  # Output: 1
print(is_bored("I am happy. I am sad! I am excited? I am bored. I am tired"))  # Output: 5
print(is_bored("What a day! I can't believe it. I am speechless! I never expected this? Wow!"))  # Output: 3
print(is_bored("This is amazing. Absolutely fantastic! Unbelievable?"))  # Output: 0
print(is_bored("I think, therefore I am. I can't. I won't! I did? I should!"))  # Output: 5

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