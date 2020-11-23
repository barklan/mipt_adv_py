
from itertools import product
import pytest
import sys, itertools
sys.path.append('..')
from w8_4 import get_cartesian_product


def test_product():
    assert get_cartesian_product([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]
    assert get_cartesian_product([1, 2], [3]) == [(1, 3), (2, 3)]
    assert get_cartesian_product([1, 2, 3, 4], [5, 6, 7, 8]) == [(1, 5), (1, 6), (1, 7), (1, 8),
                                                                 (2, 5), (2, 6), (2, 7), (2, 8),
                                                                 (3, 5), (3, 6), (3, 7), (3, 8),
                                                                 (4, 5), (4, 6), (4, 7), (4, 8)]
