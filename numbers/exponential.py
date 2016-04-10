def exponential_recursion(x, n):
    """Recursive exponential by squaring."""
    if n < 0:
        return exponential_recursion(1.0 / x, -n)
    elif n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        return exponential_recursion(x * x, n / 2)
    else:
        return exponential_recursion(x * x, (n - 1) / 2)


def exponential_iterative(x, n):
    """Iterative exponential by squaring."""
    if n < 0:
        x = 1.0 / x
        n = -n
    if n == 0:
        return 1
    y = 1
    while n > 1:
        if n % 2 == 0:
            x = x * x
            n = n / 2
        else:
            y = y * x
            x = x * x
            n = (n - 1) / 2
    return x * y

if __name__ == '__main__':
    assert exponential_recursion(5, 4) == 625
    assert exponential_recursion(8, -1) == 0.125
    assert exponential_iterative(5, 4) == 625
    assert exponential_iterative(8, -1) == 0.125
