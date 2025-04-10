def is_anagram_2_dicts(line_a: str, line_b: str) -> bool:
    if not isinstance(line_a, str) or not isinstance(line_b, str):
        raise TypeError("Both stings must be str")

    if len(line_a) != len(line_b):
        return False

    count_a, count_b = {}, {}

    for char in line_a:
        count_a[char] = count_a.get(char, 0) + 1

    for char in line_b:
        count_b[char] = count_b.get(char, 0) + 1

    return count_a == count_b