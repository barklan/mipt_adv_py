from multiprocessing import Pool
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import List
import numpy as np
from timer import Timer


def chunker(a, n):
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

    def one_chunk_dot(a_chunk, b_chunk):
        parital_dot = 0
        for i in range(len(a_chunk)):
            parital_dot += a_chunk[i] * b_chunk[i]
        accumulator.append(parital_dot)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        a_chunked, b_chunked = chunker(a, max_threads), chunker(b, max_threads)

        for i in range(max_threads):
            executor.submit(one_chunk_dot, a_chunked[i], b_chunked[i])

    for i in accumulator:
        dot_product += i

    return dot_product


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

    max_processes_list = [1, 4]
    for max_processes in max_processes_list:
        with Timer(name=f'p={max_processes}'):
            print(dot_mp(a, b, max_processes=max_processes))
