from multiprocessing import Pool, Process, Lock
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List
import numpy as np
from timer import Timer


def chunker(a, n):
    'Splits list a in n chunks'
    a_chunked = list(np.array_split(np.array(a), n))
    a_chunked_m = [list(chunk) for chunk in a_chunked]
    return a_chunked_m


def dot(*args):
    dot = 0
    for i in args:
        dot += i[0] * i[1]
    return dot


def dot_threaded(a: List[float], b: List[float], max_threads=1) -> float:

    assert len(a) == len(b), 'This is not numpy, you shitface.'

    accumulator = []
    dot_product = 0

    def one_chunk_dot(a_chunk, b_chunk, l):
        parital_dot = 0
        for i in range(len(a_chunk)):
            parital_dot += a_chunk[i] * b_chunk[i]
        l.acquire()
        accumulator.append(parital_dot)
        l.release()

    lock = Lock()
    a_chunked, b_chunked = chunker(a, max_threads), chunker(b, max_threads)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        for i in range(max_threads):
            executor.submit(one_chunk_dot, a_chunked[i], b_chunked[i], lock)

    for i in accumulator:
        dot_product += i

    return dot_product

def one_chunk_dot_z(zipped):
    parital_dot = 0
    for k, m in zipped:
        parital_dot += k * m
    accumulator.append(parital_dot)


accumulator = []
dot_product = 0
def dot_threaded2(a: List[float], b: List[float], max_threads=1) -> float:

    assert len(a) == len(b), 'This is not numpy, you shitface.'

    # accumulator = []
    # dot_product = 0

    # def one_chunk_dot_z(zipped, l):
    #     parital_dot = 0
    #     for k, m in zipped:
    #         parital_dot += k * m
    #     accumulator.append(parital_dot)
        # return parital_dot

    # def one_chunk_dot(a_chunk, b_chunk, l):
    #     parital_dot = 0
    #     for i in range(len(a_chunk)):
    #         parital_dot += a_chunk[i] * b_chunk[i]
    #     l.acquire()
    #     accumulator.append(parital_dot)
    #     l.release()
        # return parital_dot
        # l.acquire()
        # accumulator.append(parital_dot)
        # l.release()

    lock = Lock()
    a_chunked, b_chunked = chunker(a, max_threads), chunker(b, max_threads)
    zipped = zip(a, b)

    print('milestone 1')

    with ProcessPoolExecutor(max_workers=max_threads) as executor:
        for parital_dot in executor.map(one_chunk_dot_z, (zipped)):
            print('inside')
            # accumulator.append(parital_dot)

    # for i in accumulator:
    #     dot_product += i

    # return dot_product





def dot_mp(a: List[float], b: List[float], max_processes=1) -> float:
    
    '''
    Not working properly
    '''

    dot_product = 0


    pool = Pool(processes=max_processes)
    results = [pool.apply_async(dot, args=list(zip(a, b)))]
    output = [p.get() for p in results]
    for partial in output:
        dot_product += partial

    return dot_product


if __name__ == '__main__':
    a = list(np.random.randn(int(1e6)))
    b = list(np.random.randn(int(1e6)))


    # with threaded function
    a_list, b_list = list(a), list(b)
    max_threads_list = [1, 4]
    for max_threads in max_threads_list:
        with Timer(name=f'p=1;thr={max_threads}'):
            print(dot_threaded(a_list, b_list, max_threads=max_threads))

    
    # with threaded function
    a_list, b_list = list(a), list(b)
    max_threads_list = [1, 4]
    for max_threads in max_threads_list:
        with Timer(name=f'mp;p={max_threads}'):
            dot_threaded2(a_list, b_list, max_threads=max_threads)
            for i in accumulator:
                dot_product += i
            print(dot_product)
