'''
Do not try to run this on Windows. It's not worth the time...
'''

from aiohttp import ClientSession
from aiofile import AIOFile, Writer, async_open
import asyncio
from bs4 import BeautifulSoup


async def fetch_links_and_pass(url: str, session: ClientSession, afp) -> None:
    async with session.get(url) as response:
        html = await response.text()
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')
    for link in links:
        await afp.write(str(link) + '\n')


async def main(in_file, out_file):

    with open(in_file, 'r', encoding='utf-8') as f:
        urls_to_crawl = [line.strip() for line in f.readlines()]

    with open(out_file, 'w') as f:
        pass

    async with async_open(out_file, 'a', encoding='utf-8') as afp:
        async with ClientSession() as session:
            tasks = [asyncio.create_task(fetch_links_and_pass(url, session, afp))
                    for url in urls_to_crawl]
            await asyncio.gather(*tasks)


asyncio.run(main('urls.txt', 'found.txt'))