import multiprocessing as mp


# basic functions
def f1(x):
    return x*x


def f2(name):
    print('hello', name)


def foo(q):
    q.put('hello')


if __name__ == '__main__':

    # basic example of multiprocessing
    with mp.Pool(4) as p:
        print(p.map(f1, [1, 2, 3]))


    # trivial example of multiprocessing using Process
    p = mp.Process(target=f2, args=('bob',))
    p.start()
    p.join()