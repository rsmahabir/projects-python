def factorial_recursion(n):
    """Calculate n factorial using recursion."""
    if n == 1:
        return 1
    return n * factorial_recursion(n - 1)


def factorial_loops(n):
    """Calculate n factorial using loops."""
    factorial = 1
    for x in xrange(1, n + 1):
        factorial *= x
    return factorial


def factorial_lambda(n):
    """Calculate n factorial using reduce and lambda."""
    vals = [x for x in xrange(1, n + 1)]
    return reduce(lambda x, y: x * y, vals)


if __name__ == '__main__':
    assert factorial_recursion(5) == 120
    assert factorial_loops(5) == 120
    assert factorial_lambda(5) == 120
