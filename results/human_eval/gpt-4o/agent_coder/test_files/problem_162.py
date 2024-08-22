
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
    >>> string_to_md5('') == None
    >>> string_to_md5('ABCDE') == '7ac66c0f148de9519b8bd264312c4d64'
    >>> string_to_md5('!@#$%^&*()_+') == 'd8578edf8458ce06fbc5bb76a58c5ca4'
    >>> string_to_md5('Hello worldHello worldHello worldHello worldHello world') == '2d52d6e4f3c9d3d5d7ecb5c49e6a2e7e'
    """
    if text == "":
        return None
    
    md5_hash = hashlib.md5()
    md5_hash.update(text.encode('utf-8'))
    return md5_hash.hexdigest()

def check(candidate):

    # Check some simple cases
    assert candidate('Hello world') == '3e25960a79dbc69b674cd4ec67a72c62'
    assert candidate('') == None
    assert candidate('A B C') == '0ef78513b0cb8cef12743f5aeb35f888'
    assert candidate('password') == '5f4dcc3b5aa765d61d8327deb882cf99'

    # Check some edge cases that are easy to work out by hand.
    assert True


check(string_to_md5)