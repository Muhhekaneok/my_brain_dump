import math


def is_prime_number(x: int) -> bool:
    if not isinstance(x, int):
        raise TypeError("Input must be an integer")

    if x < 2:
        raise ValueError("Input must be 2 or greater")

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_prime_number_optimized(x: int) -> bool:
    if not isinstance(x, int):
        raise TypeError("Input must be an integer")

    if x < 2:
        raise ValueError("Input must be 2 or greater")

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
