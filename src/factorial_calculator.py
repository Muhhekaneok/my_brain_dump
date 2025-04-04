def get_factorial(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise TypeError("Input must be a non-negative number")

    if n <= 1:
        return 1
    return get_factorial(n - 1) * n


print(get_factorial(-5))
