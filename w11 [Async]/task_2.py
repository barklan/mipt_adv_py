from collections import namedtuple
import time
import asyncio
from concurrent.futures import FIRST_COMPLETED
import aiohttp

Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service):
    # получение ip


async def asynchronous():
    # TODO:
    # создание футур для сервисов
    # используйте FIRST_COMPLETED
    concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)


asyncio.run(asynchronous())
