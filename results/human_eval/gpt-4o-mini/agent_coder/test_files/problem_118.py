
def get_closest_vowel(word):
    """You are given a word. Your task is to find the closest vowel that stands between 
    two consonants from the right side of the word (case sensitive).
    
    Vowels in the beginning and ending doesn't count. Return empty string if you didn't
    find any vowel met the above condition. 

    You may assume that the given string contains English letter only.

    Example:
    get_closest_vowel("yogurt") ==> "u"
    get_closest_vowel("FULL") ==> "U"
    get_closest_vowel("quick") ==> ""
    get_closest_vowel("ab") ==> ""
    """


def get_closest_vowel(word):
    vowels = set('aeiouAEIOU')
    last_char = ''
    vowel_found = ''

    for char in reversed(word):
        if char in vowels:
            if last_char and last_char not in vowels:
                if not vowel_found:
                    vowel_found = char
        elif char.isalpha():  # Considering only letters, ignore others
            last_char = char
        
        # If we already found a valid vowel surrounded by consonants, we can stop
        if last_char and vowel_found:
            break

    return vowel_found

def check(candidate):

    # Check some simple cases
    assert candidate("yogurt") == "u"
    assert candidate("full") == "u"
    assert candidate("easy") == ""
    assert candidate("eAsy") == ""
    assert candidate("ali") == ""
    assert candidate("bad") == "a"
    assert candidate("most") == "o"
    assert candidate("ab") == ""
    assert candidate("ba") == ""
    assert candidate("quick") == ""
    assert candidate("anime") == "i"
    assert candidate("Asia") == ""
    assert candidate("Above") == "o"

    # Check some edge cases that are easy to work out by hand.
    assert True


check(get_closest_vowel)