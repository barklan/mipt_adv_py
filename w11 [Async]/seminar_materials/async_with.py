import asyncio

"""
with open('1.txt') as f:
    print(1)


class MyClass:
    # Non-asynchronous
    def __enter__(self):
        return 1
    def __exit__(self):
        return 1
    # Async
    def __aenter__(self):
        pass
    def __aexit__(self):
        pass
    
"""


async def func1(a, lock):
    async with lock:
        await asyncio.sleep(1)
        print(a)
        await asyncio.sleep(1)


async def lock_manager():
    lock = asyncio.Lock()
    await asyncio.gather(*[func1(i, lock) for i in range(10)])


if __name__ == '__main__':
    asyncio.run(lock_manager())
