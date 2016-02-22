from pixelcolor import PixelColor


def _border_scan(range_x, range_y):
    search_space = []
    for x in range_x:
        for y in range_y:
            search_space.append([x, y])
    return search_space


def _create_search_space(distance):
    rng_r = range(-distance, distance + 1, 1)
    rng_l = range(distance - 1, -distance + 1)
    extremes = [-distance, distance]
    return _border_scan(rng_r, extremes) + _border_scan(extremes, rng_l)


def generate_sign_permutation(el):
    """
    :param el: a tuple without sign
    :return: a tuple
    Possible permutations
        000 --> perfect match
        100 --> 100 + -100
        010 --> 010 + 0-10
        001 --> 001 + 00-1
        110 --> 110 + -110 + 1-10 + -1-10
        101 --> 101 + -101 + 10-1 + -10-1
        011 --> 011 + 0-11 + 01-1 + 0-1-1
        111 --> 111 + -111 + 1-11 + 11-1 + -1-11 + -11-1 + -1-1-1 + 1-1-1
    """

    # 100 --> 100 + -100
    if el[0] > 0 and el[1] == 0 and el[2] == 0:
        return [el, (-el[0], el[1], el[2])]

    # 010 --> 010 + 0-10
    if el[0] == 0 and el[1] > 0 and el[2] == 0:
        return [el, (el[0], -el[1], el[2])]

    # 001 --> 001 + 00-1
    if el[0] == 0 and el[1] == 0 and el[2] > 0:
        return [el, (el[0], el[1], -el[2])]

    # 110 --> 110 + -110 + 1-10 + -1-10
    if el[0] > 0 and el[1] > 0 and el[2] == 0:
        return [el, (-el[0], el[1], el[2]), (el[0], -el[1], el[2]), (-el[0], -el[1], el[2])]

    # 101 --> 101 + -101 + 10-1 + -10-1
    if el[0] > 0 and el[1] == 0 and el[2] > 0:
        return [el, (-el[0], el[1], el[2]), (el[0], el[1], -el[2]), (-el[0], el[1], -el[2])]

    # 011 --> 011 + 0-11 + 01-1 + 0-1-1
    if el[0] == 0 and el[1] > 0 and el[2] > 0:
        return [el, (el[0], -el[1], el[2]), (el[0], el[1], -el[2]), (el[0], -el[1], -el[2])]

    # 111 --> 111 + -111 + 1-11 + 11-1 + -1-11 + -11-1 + -1-1-1 + 1-1-1
    if el[0] > 0 and el[1] > 0 and el[2] > 0:
        return [el, (-el[0], el[1], el[2]), (el[0], -el[1], el[2]), (el[0], el[1], -el[2]), (-el[0], -el[1], el[2]),
                (-el[0], el[1], -el[2]), (-el[0], -el[1], -el[2]), (el[0], -el[1], -el[2])]


def generate_permutations(search_space):
    """
    Given a search space list, return an expanded search space list that includes negative directions
    """
    expanded_ss = []
    for sp in search_space:
        new_se = generate_sign_permutation(sp)
        expanded_ss.extend(new_se)
    return expanded_ss


def generate_search_space(max_edit_distance):
    search_space = []
    max_edit_distance += 1
    for x in range(0, max_edit_distance, 1):
        for y in range(0, max_edit_distance - x, 1):
            for z in range(max_edit_distance - x - y - 1, max_edit_distance - x - y, 1):
                search_space.append((x, y, z))
    return search_space


def _radial_search_match(matrix, x, y, z):
    distance = 1
    max_distance = len(matrix)
    while distance < max_distance:
        search_space = generate_search_space(distance)
        for el in search_space:
            exp_sp = generate_sign_permutation(el)
            for sp in exp_sp:
                m_x = x + sp[0]
                m_y = y + sp[1]
                m_z = z + sp[2]
                if 0 <= m_x < max_distance and 0 <= m_y < max_distance and 0 <= m_z < max_distance:
                    candidate = matrix[m_x][m_y][m_z]
                    if candidate:
                        return PixelColor(m_x, m_y, m_z)
        distance += 1
    return False


def find_nearest_match(matrix, pixelcolor):
    perfect_hit = matrix[pixelcolor.red][pixelcolor.green][pixelcolor.blue]
    if perfect_hit:
        return pixelcolor
    else:
        not_perfect_hit = _radial_search_match(matrix, *pixelcolor.as_triple())
        return not_perfect_hit
