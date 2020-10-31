
import numpy as np

def my_zip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)

        
def test_zip():
    a = ['a', 'b', 'c']
    b = [1, 2, 3]
    for pair in zip(my_zip(a, b), zip(a, b)):
        assert pair[0] == pair[1]


def my_map(func, iterable):
    for i in iterable:
        yield func(i)
        
    
def test_map():
    f = np.sin
    it = [1, 2, 3]
    for pair in zip(my_map(f, it), map(f, it)):
        assert pair[0] == pair[1]


def my_enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
        
        
def test_enumerate():
    a = ['a', 'b', 'c']
    for pair in zip(my_enumerate(a), enumerate(a)):
        assert pair[0] == pair[1]
