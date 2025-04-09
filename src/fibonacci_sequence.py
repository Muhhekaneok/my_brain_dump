def get_fibonacci_seq(n: int) -> list:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")

    fibo = [0, 1]
    for _ in range(2, n + 1):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo