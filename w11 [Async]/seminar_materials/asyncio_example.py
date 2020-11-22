import asyncio
import random


async def main():
    print('main: hello')
    fut = another()
    print('main: after another() call')
    await asyncio.sleep(1)
    print('main: slept enough, wait for `fut`')
    result = await fut
    print(f'main: gained result {result} from `another`')
    return result


async def another():
    print('another: start')
    await asyncio.sleep(random.randint(1, 5))
    print('another: stop')
    return 5


if __name__ == '__main__':
    asyncio.run(asyncio.gather(*(main(), another())))
