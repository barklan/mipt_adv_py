import asyncio


async def mygen():
    for i in range(5):
        yield i


async def main():
    all = [i async for i in mygen()]
    filtered = [j async for j in mygen() if not (j // 3 % 5)]
    return all, filtered


if __name__ == '__main__':
    all, filtered = asyncio.run(main())
    print(all)
    print(filtered)
