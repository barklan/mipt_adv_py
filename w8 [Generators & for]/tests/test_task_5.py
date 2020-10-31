
from itertools import permutations


def get_permutations(s, n):
    return sorted([''.join(x) for x in permutations(s, n)])


def test_permutations():
    assert get_permutations("cat", 2) == ["ac", "at", "ca", "ct", "ta", "tc"]
    assert get_permutations('dog', 1) == ['d', 'g', 'o']
