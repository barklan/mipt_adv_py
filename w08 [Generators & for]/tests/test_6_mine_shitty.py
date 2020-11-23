from itertools import combinations
import sys, itertools, random
sys.path.append('..')
from w8_6 import get_combinations


def test_combinations():
    assert get_combinations("cat", 2) == ["a", "c", "t", "ac", "at", "ct"]
    assert get_combinations('dog', 3) == ['d', 'g', 'o', 'dg', 'do', 'go', 'dgo']
