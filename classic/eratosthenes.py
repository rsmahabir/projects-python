def eratosthenes(limit):
    """Sieve of Erastothenes. Not efficent for high limits."""
    if limit <= 1:
        raise ValueError
    P = [True] * limit
    P[0] = False
    P[1] = False
    for i, p in enumerate(P):
        if p is True:
            yield i
            for x in xrange(i * i, limit, i):
                P[x] = False

if __name__ == '__main__':
    print list(eratosthenes(100))
