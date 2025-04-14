def get_bubble_sort(array: list) -> list:
    if not isinstance(array, list):
        raise TypeError("Input must be a list")

    n = len(array)

    for i in range(n):
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    return array


def get_bubble_sort_optimized(array) -> list:
    if not isinstance(array, list):
        raise TypeError("Input must be a list")

    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break

    return array
