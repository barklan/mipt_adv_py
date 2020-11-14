import pytest
import sys, random
sys.path.append('..')
from w8_3 import my_zip, my_map, my_enumerate


@pytest.mark.parametrize("a,b",[(['A','B','C'],[1,2,3]),(['x','y','z'],[2,14,6]),(['0','0','0'],[0,0,0])])
def test_zip(a,b):
    for pair in zip(my_zip(a, b), zip(a, b)):
        assert pair[0] == pair[1]


@pytest.mark.parametrize("func,it",[(int,['1','2','3','4','5']) ,(abs,[-1, 0,-10]) ])
def test_map(func,it):
    for pair in zip(list(my_map(func,it)), list(map(func,it))):
        assert pair[0] == pair[1]


@pytest.mark.parametrize("list1",[(['str1', 'str2', 'str3']), (['1', '2', '3', '4'])])
def test_enumerate(list1):
    for pair in zip(my_enumerate(list1), enumerate(list1)):
        assert pair[0] == pair[1]
