def get_reverse(line: str) -> str:
    if not isinstance(line, str):
        raise TypeError("Input must be a string")

    result = ""
    for i in range(len(line) - 1, -1, -1):
        result += line[i]
    return result