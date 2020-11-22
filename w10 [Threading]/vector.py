# from multiprocessing import Pool, Process, Lock
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor  # , ProcessPoolExecutor
from typing import List
from timer import Timer
from multiprocessing import Pool

import numpy as np
import pandas as pd


def chunker(a, n):
    'Splits list a in n chunks'
    return (np.array_split(a, n))
    a_chunked_m = [list(chunk) for chunk in a_chunked]
    # return a_chunked_m


def dot_threaded(a: List[float], b: List[float], max_workers=1) -> float:

    assert len(a) == len(b)

    accumulator = []
    dot_product = 0

    def one_chunk_dot(a_chunk, b_chunk):
        parital_dot = 0
        for i in range(len(a_chunk)):
            parital_dot += a_chunk[i] * b_chunk[i]
        accumulator.append(parital_dot)

    a_chunked, b_chunked = chunker(a, max_workers), chunker(b, max_workers)

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i in range(max_workers):
            executor.submit(one_chunk_dot, a_chunked[i], b_chunked[i])

    for i in accumulator:
        dot_product += i

    return dot_product


def dot(v1, v2):
    dot = 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
    return dot


def dot_mp(a, b, max_workers=1):

    with Pool(max_workers) as p:
        results = [p.apply(np.dot, args=(v1, v2))
                   for v1, v2 in zip(np.array_split(a, max_workers),
                                     np.array_split(b, max_workers))]
        # accumulator = p.map(dot, a, b)

    dot_product = sum(results)

    assert round(dot_product, 5) == round(np.dot(np.array(a), np.array(b)), 5)

    return dot_product


if __name__ == '__main__':
    Timer.timers = {}
    df = pd.DataFrame(columns=['index', 0]) 
    
    for i in range(5):
    
        a, b = (np.random.randn(100_000) for i in range(2))

        # # with threaded function
        max_workers_list = [1, 2, 4, 8, 16]
        for max_workers in max_workers_list:
            with Timer(name=f'p=1;thr={max_workers}'):
                print(dot_threaded(a, b, max_workers=max_workers))

        # with mp
        max_workers_list = [1, 2, 4, 8, 16]
        for max_workers in max_workers_list:
            with Timer(name=f'p={max_workers}'):
                print(dot_mp(a, b, max_workers=max_workers))
        

        df_temp = pd.DataFrame.from_dict(Timer.timers, orient='index').reset_index()
        df = df.append(df_temp, ignore_index=True)
        Timer.timers = {}

    df.rename(columns = {'index':'name', 0:'time'}, inplace = True)
    print(df)
    df.to_csv('vscode.csv', index=True)
