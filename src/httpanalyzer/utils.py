

def url_decode(string: str) -> str:
    """
    Decode the percent-encoded parts of the url.
    :param string: the lowercase url
    :return: the percent-decoded url
    """
    modified_string = string
    for i in range(32, 127):
        modified_string = modified_string.replace(f"#{hex(i)[2:]}", chr(i))
    if modified_string != string:
        return url_decode(modified_string)
    else:
        return modified_string
