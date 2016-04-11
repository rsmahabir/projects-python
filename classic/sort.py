def merge(left, right):
    """Merge two lists together in sorted order."""
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    for l in left:
        result.append(l)
    for r in right:
        result.append(r)
    return result


def merge_sort_td(vals):
    """Recursively sort list top down."""
    if len(vals) <= 1:
        return vals
    left = vals[1::2]
    right = vals[::2]
    left = merge_sort_td(left)
    right = merge_sort_td(right)
    return merge(left, right)


def bubble_sort(vals):
    """Bubble sort list with n-1 optimization."""
    n = len(vals)
    while True:
        swapped = False
        for i in xrange(1, n):
            if vals[i - 1] > vals[i]:
                vals[i - 1], vals[i] = vals[i], vals[i - 1]
                swapped = True
        if swapped is False:
            break
    return vals


if __name__ == '__main__':
    assert merge([1, 3], [2, 4]) == [1, 2, 3, 4]
    assert merge_sort_td([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]
