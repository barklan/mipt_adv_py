
from itertools import groupby


def get_combinations_with_r(s, n):
    return sorted([''.join(sorted(x)) for x in combinations_with_replacement(s, n)])

    
def compress_string(s):
    groups = []
    uniquekeys = []
    for k, g in groupby(s):
        groups.append(len(list(g)))
        uniquekeys.append(int(k))
    return list(zip(groups, uniquekeys))

        
def test_compress_string():
    assert compress_string('1222311') == [(1, 1), (3, 2), (1, 3), (2, 1)]
    assert compress_string('12223111') == [(1, 1), (3, 2), (1, 3), (3, 1)]
    compress_string('144423455553333532341') == [(1, 1), (3, 4), (1, 2), (1, 3),
                                                 (1, 4), (4, 5), (4, 3), (1, 5),
                                                 (1, 3), (1, 2), (1, 3), (1, 4),
                                                 (1, 1)]
