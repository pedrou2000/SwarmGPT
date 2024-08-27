
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
    >>> string_to_md5('Python') == 'a7f5f35426b927411fc9231b56382173'
    >>> string_to_md5('!@#$%^&*()') == '05b28d17a7b6e7024b6e5d8cc43a8bf7'
    >>> string_to_md5('') == None
    """
    if text == "":
        return None
    
    # Create an MD5 hash object
    md5_hash = hashlib.md5()
    
    # Update the hash object with the bytes of the input text
    md5_hash.update(text.encode('utf-8'))
    
    # Get the hexadecimal representation of the hash
    return md5_hash.hexdigest()

# Test cases to verify the function
assert string_to_md5('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
assert string_to_md5('Python') == 'a7f5f35426b927411fc9231b56382173'
assert string_to_md5('!@#$%^&*()') == '05b28d17a7b6e7024b6e5d8cc43a8bf7'
assert string_to_md5('') == None

print("All tests passed!")

def check(candidate):

    # Check some simple cases
    assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert candidate('') == None
    assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
    assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'

    # Check some edge cases that are easy to work out by hand.
    assert True


check(string_to_md5)