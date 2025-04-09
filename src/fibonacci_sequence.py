def get_fibonacci_seq(n: int) -> list:
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative number")

    if n == 0:
        return []
    if n == 1:
        return [0]

    fibo = [0, 1]
    for _ in range(2, n):
        fibo.append(fibo[-1] + fibo[-2])
    return fibo