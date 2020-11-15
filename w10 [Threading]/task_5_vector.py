import os
import threading
from concurrent.futures import ThreadPoolExecutor
from typing import List
import logging
import time
import numpy as np


def list_dot(a: List[float], b: List[float], max_threads=1) -> float:

    assert len(a) == len(b), 'This is not numpy, you shitface. No broadcasting here.'

    to_accumulate = []
    dot_product = 0

    def chunker(a, n):
        a_chunked = [a[i:i + n] for i in range(0, len(a), n)]
        return a_chunked

    def one_thread_dot(a_chunk, b_chunk):
        print(a_chunk)

        parital_dot = 0
        for i in len(a_chunk):
            parital_dot += a_chunk[i] * b_chunk[i]
        to_accumulate.append(parital_dot)

    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        a_chunked, b_chunked = chunker(a, max_threads), chunker(b, max_threads)

        for i in range(max_threads):
            executor.submit(one_thread_dot, (a_chunked[i], b_chunked[i]))

    print(to_accumulate)
    for i in to_accumulate:
        dot_product += i

    return dot_product


if __name__ == '__main__':
    print(list_dot([3], [4]))
