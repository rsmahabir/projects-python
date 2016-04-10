def prime_sieve(limit):
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
    num = 49
    primes = [p for p in prime_sieve(num)]
    factors = []
    for p in primes:
        if num % p == 0:
            factors.append(p)
    for f in factors:
        print f
