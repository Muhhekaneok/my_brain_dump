def is_anagram_2_dicts(line_a: str, line_b: str) -> bool:
    if not isinstance(line_a, str) or not isinstance(line_b, str):
        raise TypeError("Both lines must be str type")

    if len(line_a) != len(line_b):
        return False

    line_a = line_a.lower()
    line_b = line_b.lower()

    count_a, count_b = {}, {}

    for char in line_a:
        count_a[char] = count_a.get(char, 0) + 1

    for char in line_b:
        count_b[char] = count_b.get(char, 0) + 1

    return count_a == count_b


def is_anagram_1_dict(line_a: str, line_b: str) -> bool:
    if not isinstance(line_a, str) or not isinstance(line_b, str):
        raise TypeError("Both lines must be str type")

    if len(line_a) != len(line_b):
        return False

    line_a = line_a.lower()
    line_b = line_b.lower()

    count_char = {}

    for char in line_a:
        count_char[char] = count_char.get(char, 0) + 1

    for char in line_b:
        if char not in count_char:
            return False
        count_char[char] -= 1
        if count_char[char] < 0:
            return False

    return True
