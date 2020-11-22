import asyncio


async def long_coroutine():
    await asyncio.sleep(7)


async def wait():
    try:
        print('Trying to wait for coroutine')
        await asyncio.wait_for(long_coroutine(), timeout=3)
    except asyncio.TimeoutError:
        print('Timeout for coroutine!')


if __name__ == '__main__':
    asyncio.run(wait())
