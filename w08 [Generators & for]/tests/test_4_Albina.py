import sys, itertools
sys.path.append('..')
from w8_4 import get_cartesian_product

def test_for_cartesian_product(data1, data2, data3):
    for item in [data1, data2], [data1, data3], [data2, data3]:
        for i in range (5):
            assert get_cartesian_product(item[0][i:], item[1][i:]) == list(itertools.product(item[0][i:], item[1][i:]))
            assert get_cartesian_product(item[0][:i], item[1][:i]) == list(itertools.product(item[0][:i], item[1][:i]))
