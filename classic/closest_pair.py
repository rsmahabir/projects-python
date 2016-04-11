def euclidian(p1, p2):
    """Calculate euclidian distance between a pair of 2d points."""
    return (((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)) ** 0.5


def closest_pair_brute(pts):
    """Find the closest pair by checking all combinations of points."""
    closest_pair = pts[:2]
    min_dist = euclidian(*closest_pair)
    num_pts = len(pts)
    for i in xrange(num_pts):
        for j in xrange(i + 1, num_pts):
            pair = (pts[i], pts[j])
            dist = euclidian(*pair)
            if dist < min_dist:
                min_dist = dist
                closest_pair = pair
    return min_dist, closest_pair

if __name__ == '__main__':
    assert euclidian((0, 0), (0, 1)) == 1
    pts = ((7, 14),
           (8, 15),
           (7, 16),
           (1, 12),
           (7, 8),
           (7, 17),
           (2, 7),
           (8, 16),
           (2, 10),
           (17, 18),
           (10, 15),
           (1, 4),
           (2, 19),
           (3, 18),
           (4, 9),
           (8, 11),
           (11, 13),
           (3, 12),
           (1, 14),
           (1, 15))
    dist, pair = closest_pair_brute(pts)
    assert dist == 1.0
    assert pair == ((8, 15), (8, 16))
