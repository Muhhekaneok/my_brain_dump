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


def get_sieve_of_eratosthenes(n: int) -> list:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    if n < 2:
        return []

    sieve_list = [True] * (n + 1)
    sieve_list[0], sieve_list[1] = False, False

    for i in range(2, int(math.sqrt(n)) + 1):
        if sieve_list[i]:
            for j in range(i * i, n + 1, i):
                sieve_list[j] = False

    return [index for index, is_prime in enumerate(sieve_list) if is_prime]