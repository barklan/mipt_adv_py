# Asynchronous Programming and web scraping



- [`asyncio` — Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/#a-full-program-asynchronous-requests)


## asyncio & aiohttp
Число в скобках - количество баллов.

_ДЗ частично взято с [соответствующей лабы](http://cs.mipt.ru/advanced_python/lessons/lab11.html)_.

1. (2) В папке `w11/webserver` лежит простой веб-сервер, который отвечает на `/` через 3 секунды.
Ваша задача - написать код, который осуществляет 100 запросов на этот сервер и дожидается **всех** ответов от него.
Это нужно сделать асинхронно, т.к. сервер обрабатывает каждый запрос 3 секунды.
2. (4) [Упражнение 2 с cs.mipt.ru](http://cs.mipt.ru/advanced_python/lessons/lab11.html#o2).
Узнать свой IP адрес. 
Есть куча сервисов, которые позволяют узнать ваш ip.
Но на момент запуска программы вы не знаете какой из сервисов доступен.
Вместо того, чтобы опрашивать каждый из этих сервисов последовательно, 
можно запустить все запросы конкурентно и выбрать первый успешный.
Потребуется `asyncio.wait()` и параметр `return_when`

```python
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

ioloop = asyncio.get_event_loop()
ioloop.run_until_complete(asynchronous())
```

3. (4) Напишите программу, которая открывает файл `urls.txt`, читает веб-ссылки в нем.
Затем для каждой из ссылок загрузите эту страницу, найдите в ней строку, начинающуюся со слов "\<a \>"
и запишите эту строку целиком в файл `found.txt`. Запись в файл и загрузка сайта должны быть асинхронными.
Для работы с файлами используйте `aiofile`.

# TODO
- install anaconda in wsl (already downloaded), and create env for vscode in wsl

## testing

- pytest -> hypothesis
- unittest
- doctest

## Telegram bots
- consolidate old bots
- iogram -> write a new bot

## Web Scraping

- [A Practical Introduction to Web Scraping in Python](https://realpython.com/python-web-scraping-practical-introduction/#your-first-web-scraper)
- bs4
- [`scrapy`](https://scrapy.org/)
- selenium web driver
- How to scrape for images (dynamicly?) -> for later use in CNN