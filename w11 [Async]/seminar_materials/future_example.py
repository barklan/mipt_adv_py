import asyncio


async def a():
    try:
        for i in range(1, 5):
            print(f'a: i={i}')
            await asyncio.sleep(i)
    except asyncio.CancelledError:
        print('I am cancelled :(')
        return


async def create_future():
    future = asyncio.ensure_future(a())
    while not future.done():
        print('Future is not done, sleeping 1 second...')
        await asyncio.sleep(1)
        future.cancel()
    print('Future is complete!')


if __name__ == '__main__':
    asyncio.run(create_future())
