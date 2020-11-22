import asyncio


async def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print(f"Task {name}: Compute factorial({i})...")
        await asyncio.sleep(2)
        f *= i
    print(f"Task {name}: factorial({number}) = {f}")


async def print_sleep():
    print('before sleep')
    await asyncio.sleep(3.5)
    print('after sleep')


async def main():
    await asyncio.gather(
        factorial("A", 2),
        factorial("B", 3),
        factorial("C", 4),
        print_sleep(),
    )

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
