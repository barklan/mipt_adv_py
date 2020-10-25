
from itertools import accumulate
import numpy as np


def maximize(lists, m):
    
    max_list = []
    for lst in lists:
        max_list.append(max(lst)**2)
    
    return max(list(accumulate(max_list, lambda x, y : ((x + y) % 1000))))
            

def test_maximize():
    lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    assert maximize(lists, m=1000) == 206
