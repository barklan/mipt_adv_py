
def fibgen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib(n):
    f = fibgen()
    a = []
    for _ in range(n):
        a.append(next(f))
    return a


def test_fib():
    assert fib(10)[0] == 0
    assert fib(11)[3] == 2
