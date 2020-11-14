from itertools import accumulate


def maximize(lists, m):
    squared_maxes = [max(lst)**2 for lst in lists]
    polynomials = [p for p in accumulate(squared_maxes)]
    
    return max([x % m for x in polynomials])
