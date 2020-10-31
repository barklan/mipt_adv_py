
from itertools import product

def get_cartesian_product(a, b):
    return list(product(a, b))


def test_product():
    assert get_cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
