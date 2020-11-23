'''
В следующем примере мы запустим две задачи на параллельное исполнение.
'''

import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1, task2 = (asyncio.create_task(say_after(2, word))
                    for word in ('hello', 'world'))

    start = time.time()

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    finish = time.time() - start
    print(f'runtime: {finish:.2f} seconds')


asyncio.run(main())
