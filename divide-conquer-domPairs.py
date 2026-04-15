def get_x(p):
    return p[0]

def get_y(p):
    return p[1]


def count_dominating_pairs(points):
    # Presort once into x-order and y-order before recursing
    Lx = sorted(points, key=get_x)
    Ly = sorted(points, key=get_y)
    count, _ = recurse(Lx, Ly)
    return count


def recurse(Lx, Ly):
    n = len(Lx)

    # Base case: a single point has no pairs
    if n == 1:
        return 0, Ly

    # Divide by median x into left and right halves
    mid      = n // 2
    Lx_left  = Lx[:mid]
    Lx_right = Lx[mid:]
    x_prime  = Lx_left[-1][0]

    # Filter Ly into left and right, preserving y-order (O(n), no re-sorting needed)
    Ly_left  = [p for p in Ly if p[0] <= x_prime]
    Ly_right = [p for p in Ly if p[0] >  x_prime]

    # Recurse on each half
    count_L, Ly_left_sorted  = recurse(Lx_left,  Ly_left)
    count_R, Ly_right_sorted = recurse(Lx_right, Ly_right)

    # Merge: count cross-border pairs and combine the two Ly lists
    cross_count, combined_Ly = merge(Ly_left_sorted, Ly_right_sorted)

    return count_L + count_R + cross_count, combined_Ly


def merge(Ly_left, Ly_right):
    # Standard merge of two y-sorted lists into one (O(n))
    merged = []
    i, j = 0, 0
    while i < len(Ly_left) and j < len(Ly_right):
        if Ly_left[i][1] <= Ly_right[j][1]:
            merged.append((Ly_left[i],  'L')); i += 1
        else:
            merged.append((Ly_right[j], 'R')); j += 1
    while i < len(Ly_left):
        merged.append((Ly_left[i],  'L')); i += 1
    while j < len(Ly_right):
        merged.append((Ly_right[j], 'R')); j += 1

    # Scan top to bottom: when we see a left point, all right points
    # already seen have larger y and larger x, so they dominate it
    c = 0
    cross_count = 0
    for point, side in reversed(merged):
        if side == 'R':
            c += 1
        else:
            cross_count += c

    combined_Ly = [point for point, _ in merged]
    return cross_count, combined_Ly