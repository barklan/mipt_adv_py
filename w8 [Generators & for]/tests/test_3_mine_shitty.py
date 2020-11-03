import numpy as np
import sys, random
sys.path.append('..')
from w8_3 import my_zip, my_map, my_enumerate
        
def test_zip():
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    for pair in zip(my_zip(a, b), zip(a, b)):
        assert pair[0] == pair[1]

    
def test_map():
    f = np.sin
    it = [1, 2, 3]
    for pair in zip(my_map(f, it), map(f, it)):
        assert pair[0] == pair[1]
        
        
def test_enumerate():
    a = ['a', 'b', 'c']
    for pair in zip(my_enumerate(a), enumerate(a)):
        assert pair[0] == pair[1]
