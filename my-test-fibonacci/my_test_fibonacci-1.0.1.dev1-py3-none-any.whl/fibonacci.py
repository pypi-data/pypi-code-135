def fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"expect integer input, get {n}")
    if n < 0:
        raise ValueError(f"expect non-negative input, get {n}")
    if n <= 1:
        return n
    p0, p1 = 0, 1
    for _ in range(n - 1):
        p0, p1 = p1, p0 + p1
    return p1


def recursion_fibonacci(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError(f"expect integer input, get {n}")
    if n < 0:
        raise ValueError(f"expect non-negative input, get {n}")
    if n <= 1:
        return n
    return recursion_fibonacci(n - 2) + recursion_fibonacci(n - 1)
