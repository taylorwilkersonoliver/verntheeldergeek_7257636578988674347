from typing import List

this = \
    [
        "01110010",
        "10100110",
        "01001110",
        "00100110",
    ]


def run(var: List) -> str:
    out = ""
    for i in var:
        var_number = int(i[::-1], 2)
        out += chr(var_number)
    return out


if __name__ == '__main__':
    print(run(this))
