def fibonacci(n):
    """Yield fibonacci sequene to n iterations."""
    if n < 1:
        raise ValueError
    i = 0
    j = 1
    for x in xrange(n):
        if x == 0:
            yield 1
            continue
        k = i + j
        i = j
        j = k
        yield k

if __name__ == '__main__':
    seq = fibonacci(10)
    for s in seq:
        print s
