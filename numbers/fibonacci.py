def fibonacci(n):
    """Yield fibonacci sequene to n iterations."""
    if n < 1:
        raise ValueError
    i = 0
    j = 1
    yield j
    for x in xrange(n - 1):
        i, j = j, i + j
        yield j

if __name__ == '__main__':
    seq = fibonacci(10)
    for s in seq:
        print s
