def is_palindrome(line: str) -> bool:
    if not isinstance(line, str):
        raise TypeError("Expected a string")

    for i in range(len(line)):
        if line[i] != line[len(line) - i - 1]:
            return False

    return True