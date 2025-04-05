def get_factorial_recursive(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative number")

    if n <= 1:
        return 1
    return get_factorial_recursive(n - 1) * n


def get_factorial_iterative(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be non-negative number")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result