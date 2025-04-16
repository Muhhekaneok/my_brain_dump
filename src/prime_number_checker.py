def get_prime_number(x: int) -> bool:
    if not isinstance(x, int):
        raise TypeError("Input must be an integer")

    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            print()
            return False
    return True
