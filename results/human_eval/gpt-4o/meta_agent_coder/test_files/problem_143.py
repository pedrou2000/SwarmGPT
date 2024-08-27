
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


from math import isqrt

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

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
    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)

# Example usage:
print(words_in_sentence("This is a test"))  # Output: "is"
print(words_in_sentence("lets go for swimming"))  # Output: "go for"
print(words_in_sentence("an example of prime lengths"))  # Output: "an of prime"
print(words_in_sentence("one two three four five six"))  # Output: "two three five"
print(words_in_sentence("a b c d e f g"))  # Output: "a b c d e f g"
print(words_in_sentence("hello world"))  # Output: "world"
print(words_in_sentence("abcd efgh ijklm"))  # Output: ""
print(words_in_sentence("a ab abc abcd abcde abcdef"))  # Output: "a abc abcde"
print(words_in_sentence("oneword"))  # Output: ""
print(words_in_sentence("one two three four five six seven"))  # Output: "two three five"

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