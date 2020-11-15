import os
import threading
from typing import List


def ping(ips: List[str]) -> list:
    for ip in ips:
        ping_output = os.popen('ping ' + ip)
        # print("... pinging ", ip)
        _ = ping_output.read()


def ping_threaded(ips: List[str]) -> list:
    pass


ips = ['google.com',
       'youtube.com',
       'wikipedia.org',
       'yahoo.com',
       'yandex.ru',
       'ya.ru',
       'rambler.ru',
       'mail.ru']


if __name__ == '__main__':

    print(ping(ips))
