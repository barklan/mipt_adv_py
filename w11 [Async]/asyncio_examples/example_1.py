'''
В этом примере:

    Упарвление будет передано в корутину main;
    Напечатается hello;
    Управление будет передано в корутину sleep;
    В течении одной секунды программа "спит";
    Управление вернется в main;
    Напечатается wolrd;
    Корутина main, а далее сама программа завершаются.
'''


import asyncio


async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')


loop = asyncio.get_event_loop()
# Blocking call which returns when the main() coroutine is done
loop.run_until_complete(main())
loop.close()

# Python 3.7+
asyncio.run(main())
