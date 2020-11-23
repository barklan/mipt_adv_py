from itertools import permutations


def get_permutations(s, n):
    return sorted([''.join(x) for x in permutations(s, n)])
