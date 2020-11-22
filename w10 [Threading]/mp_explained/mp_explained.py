import multiprocessing as mp


# basic function
def f1(x):
    return x*x


if __name__ == '__main__':

    # basic example of multiprocessing
    with mp.Pool(4) as p:
        print(p.map(f1, [1, 2, 3]))