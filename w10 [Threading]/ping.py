import os
import threading
import concurrent.futures
from typing import List
import logging
import time


def ping(ips: List[str]) -> List[str]:
    return [os.popen('ping ' + ip).read() for ip in ips]


def ping_threaded(ips: List[str], max_threads: int = 8) -> List[str]:
    output = []

    def thread_ping(ip):
        output.append(os.popen('ping ' + ip).read())

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_threads) as executor:
        executor.map(thread_ping, ips)

    return output


ips = ['google.com',
       'youtube.com',
       'wikipedia.org',
       'yahoo.com',
       'vk.com',
       'ranepa.ru',
       'rambler.ru',
       'softbox.tv']


if __name__ == '__main__':

    print(ping_threaded(ips))
