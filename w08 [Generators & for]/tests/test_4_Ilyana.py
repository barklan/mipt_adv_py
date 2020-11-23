import itertools
import pytest
import sys, itertools
sys.path.append('..')
from w8_4 import get_cartesian_product


@pytest.mark.parametrize("a,b", [([1, 2, 3],[1, 1, 1]), ([1,2],[1,1]), ([4, 5, 9],[10, 3, 8])])
def test_product(a, b):
    assert get_cartesian_product(a,b) == list(itertools.product(a, b))
