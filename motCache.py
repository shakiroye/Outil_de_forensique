import re

def get_strings(file_name):
    with open(file_name, "rb") as file:
        content = file.read()
    _re = re.compile("[\S\s]{4,}")
    for match in _re.finditer(content.decode("utf8", "backslashreplace")):
        print(match.group())

get_strings("resources/lorem.pdf")