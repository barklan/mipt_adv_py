import pytest
import itertools
import sys, itertools, random
sys.path.append('..')
from w8_7 import get_combinations_with_r


@pytest.mark.parametrize("s,n", [(['print'],(1)), (['lesson'],(2)), (['home'],(3))])
def test_combinations_with_r(s, n):
    assert get_combinations_with_r(s, n) == sorted([''.join(sorted(x)) for x in itertools.combinations_with_replacement(s, n)])
