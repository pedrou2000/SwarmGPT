
def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """


import hashlib

def string_to_md5(text):
    """
    Given a string 'text', return its md5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    """
    # Step 1: Check if the input text is empty
    if not text:
        return None

    # Step 2: Compute the MD5 hash of the input text
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Encode the input text to bytes and update the hash object
    md5_hash.update(text.encode('utf-8'))
    
    # Retrieve the hexadecimal digest of the hash
    result = md5_hash.hexdigest()
    
    # Step 3: Return the result
    return result

# Tests
def run_tests():
    test_cases = {
        'Hello world': 'fc3ff98e8c6a0d3087d515c0473f8677',
        '!@#$%^&*()': 'b14c0b310bcd058de3134c4d04f6e6a5',
        'The quick brown fox jumps over the lazy dog': '9e107d9d372bb6826bd81d3542a419d6',
        '': None,
        'With spaces': '77eda04c3a623dcb9a6a2f3f1c9b2e51',
        'Sentence, with punctuation!': '8ff32489e2c6a0b02b0ea9667e8d6c51',
        '1234567890': 'e807f1fcf82d132f9bb018ca6738a19f',
    }

    for text, expected_md5 in test_cases.items():
        result = string_to_md5(text)
        assert result == expected_md5, f"Test failed for input '{text}'. Expected: {expected_md5}, Got: {result}"
        print(f"Test passed for input '{text}'.")

if __name__ == "__main__":
    run_tests()

def check(candidate):

    # Check some simple cases
    assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert candidate('') == None
    assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
    assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'

    # Check some edge cases that are easy to work out by hand.
    assert True


check(string_to_md5)