def collatz_recursive(n, count=0):
    """Recursive implementation of Collatz Conjecture."""
    if n <= 1 and count == 0:
        raise ValueError
    if n == 1:
        return count
    if n % 2 == 0:
        return collatz_recursive(n / 2, count + 1)
    else:
        return collatz_recursive((n * 3) + 1, count + 1)


def collatz_loops(n):
    """Implementation of Collatz Conjecture using loops."""
    if n <= 1:
        raise ValueError
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (n * 3) + 1
        count += 1
    return count

if __name__ == '__main__':
    assert collatz_recursive(27) == 111
    assert collatz_loops(27) == 111
