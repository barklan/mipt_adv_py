import sys
import argparse


def fibgen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib(n):
    n = int(n)
    f = fibgen()
    for _ in range(n-1):
        next(f)
    return next(f)


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', nargs='?')
    return parser


if __name__ == '__main__':
    try:
        n = int(sys.argv[1])
        print(fib(n))
    except:
        parser = createParser()
        namespace = parser.parse_args()
        print(fib(namespace.n))