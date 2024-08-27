
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """


def is_prime(n):
    """ Check if a number n is prime. """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """ Returns a string of words with prime lengths from the given sentence. """
    result = []
    words = sentence.split()
    
    for word in words:
        # Check if the length of the word is prime
        if is_prime(len(word)):
            result.append(word)
    
    # Join the results with a space and return
    return ' '.join(result)

# Example usage for testing
print(words_in_sentence("hello world"))  # Expected: "hello"
print(words_in_sentence("apple orange banana"))  # Expected: "apple orange"
print(words_in_sentence("The quick brown fox"))  # Expected: "The fox"

def check(candidate):

    # Check some simple cases
    assert candidate("This is a test") == "is"
    assert candidate("lets go for swimming") == "go for"
    assert candidate("there is no place available here") == "there is no place"
    assert candidate("Hi I am Hussein") == "Hi am Hussein"
    assert candidate("go for it") == "go for it"

    # Check some edge cases that are easy to work out by hand.
    assert candidate("here") == ""
    assert candidate("here is") == "is"


check(words_in_sentence)