

def url_decode(string: str) -> str:
    """
    Decode the percent-encoded parts of the url.
    :param string: the lowercase url
    :return: the percent-decoded url
    """
    for i in range(32, 127):
        string = string.replace(f"#{hex(i)[2:]}", chr(i))
    return string
