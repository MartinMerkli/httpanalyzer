

def url_decode(string: str) -> str:
    for i in range(32, 127):
        string = string.replace(f"#{hex(i)[2:]}", chr(i))
    return string
