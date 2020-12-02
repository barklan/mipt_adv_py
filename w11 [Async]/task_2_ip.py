from collections import namedtuple
import time
import asyncio
import concurrent.futures
from concurrent.futures import FIRST_COMPLETED
import aiohttp
from aiohttp import ClientSession


Service = namedtuple('Service', ('name', 'url', 'ip_attr'))

SERVICES = (
    Service('ipify', 'https://api.ipify.org?format=json', 'ip'),
    Service('ip-api', 'http://ip-api.com/json', 'query')
)


async def fetch_ip(service, session):
    async with session.get(service.url) as resp:
        json = await resp.json()
        return json[service.ip_attr]


async def asynchronous():
    async with ClientSession() as session:
        tasks = [asyncio.create_task(fetch_ip(service, session))
                 for service in SERVICES]
        done, pending = await asyncio.wait(tasks, timeout=None,
                                           return_when=FIRST_COMPLETED)
        for i in done:
            print(i.result())


asyncio.run(asynchronous())
