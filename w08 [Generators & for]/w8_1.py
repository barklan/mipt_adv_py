def print_map(func, iterable):
    ind = True
    while ind:
        try:
            print(func(next(iterable)))
        except StopIteration:
            ind = False


def function(x):
    return x ** 2


a = iter([1, 2, 3, 4, 5])
print_map(function, a)

