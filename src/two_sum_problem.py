def get_two_sum_indices(lst: list, s: int) -> tuple:
    if not isinstance(lst, list) or not isinstance(s, int):
        raise TypeError("Input must be list and an integer")

    seen = {}
    for i, num in enumerate(lst):
        complement = s - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return ()


print(get_two_sum_indices([], 10))