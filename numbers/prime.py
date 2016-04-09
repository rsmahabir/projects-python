def isprime(n):
    """O(sqrt(n)) prime checker."""
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0) or (n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0) or (n % (i + 2) == 0):
            return False
        i += 6
    return True


def prime_gen():
    """Brute force prime generator."""
    i = 0
    while True:
        if isprime(i):
            yield i
        i += 1

if __name__ == '__main__':
    p = prime_gen()
    for _ in xrange(10):
        print p.next()
