# Must return the index of the target value in the array using a binary search algorithm
def get_binary_search(array: list, target: int) -> int:
    if not isinstance(array, list) or not isinstance(target, int):
        raise TypeError("Inputs must be list and integer")

    left, right = 0, len(array) - 1
    array.sort()

    while left <= right:
        middle = (left + right) // 2
        if array[middle] == target:
            return middle
        elif array[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1