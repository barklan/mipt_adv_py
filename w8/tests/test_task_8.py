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
