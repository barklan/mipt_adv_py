
from itertools import accumulate


def maximize(lists, m):
    squared_maxes = [max(lst)**2 for lst in lists]
    polynomials = [p for p in accumulate(squared_maxes)]
    
    return max([x % m for x in polynomials])


def test_maximize():
    lists = [
        [5, 4],
        [7, 8, 9],
        [5, 7, 8, 9, 10]
    ]
    assert maximize(lists, m=1000) == 206
    
    lists = [
            [1000, 4],
            [7, 8, 9],
            [5, 7, 8, 9, 10]
        ]
    assert maximize(lists, 1000) == (1000 ** 2 + 9 ** 2 + 10 ** 2) % 1000
    
    lists = [
            [1, 1],
            [1, 2],
            [0, 3]
        ]
    assert maximize(lists, 10) == (1 ** 2 + 2 ** 2) % 10
