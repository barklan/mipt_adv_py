'''
Следующий пример напечатает “hello” после ожидания в 1 секунду,
а затем напечатает “world” после ожидания в 2 секунды:
'''


import asyncio
import time


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    print(f"started at {time.strftime('%X')}")

    await say_after(1, 'hello')
    await say_after(2, 'world')

    print(f"finished at {time.strftime('%X')}")

# loop = asyncio.get_event_loop()
# # Blocking call which returns when the main() coroutine is done
# loop.run_until_complete(main())
# loop.close()

asyncio.run(main())
