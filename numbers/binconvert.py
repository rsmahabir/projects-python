def bin2dec(b):
    """Convert binary string to integer."""
    if b.startswith('0b'):
        return int(b, 2)
    else:
        raise ValueError


def dec2bin(d):
    """Convert decimal number to binary string."""
    if isinstance(d, int):
        return bin(d)
    else:
        raise ValueError

if __name__ == '__main__':
    for x in xrange(10):
        assert x == bin2dec(dec2bin(x))
