from itertools import combinations_with_replacement


def get_combinations_with_r(s, n):
    return sorted([''.join(sorted(x)) for x in combinations_with_replacement(s, n)])
