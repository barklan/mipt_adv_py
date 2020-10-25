from itertools import combinations
from operator import itemgetter, attrgetter


def get_combinations(s, n):
    a = sorted([''.join(sorted(x)) for i in range(1, n+1) for x in combinations(s, i)])
    a.sort(key=lambda x: len(x))
    return a


def test_combinations():
    assert get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"]
