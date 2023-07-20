from typing import List

this = \
    [
        "01110010",
        "10100110",
        "01001110",
        "00100110",
    ]


def reveal(var: List) -> str:
    """Reveal obfuscated text."""
    out = ""
    for i in var:
        var_number = int(i[::-1], 2)
        out += chr(var_number)
    return out


def obfuscate(var: str) -> List:
    """Obfuscate text."""
    out = []
    for i in var:
        out.append(str(bin(ord(i)))[::-1])
    return out


if __name__ == '__main__':
    print(reveal(this))
    print(reveal(obfuscate('Anything')))
