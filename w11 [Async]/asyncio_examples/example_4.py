'''
asyncio абстракции
'''

import asyncio


async def compute(a, b):
    print('Compute...')
    await asyncio.sleep(1.0)
    return a + b


async def print_sum(a, b):
    result = await compute(a, b)
    print('{} + {} = {}'.format(a, b, result))


loop = asyncio.get_event_loop()
loop.run_until_complete(print_sum(1, 2))
loop.close()
