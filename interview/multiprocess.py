from multiprocessing import Pool
from multiprocessing.pool import ThreadPool
from functools import partial
from concurrent.futures import ThreadPoolExecutor

import aiohttp
import aiofiles
import asyncio

import requests

url = 'https://movie.douban.com/top250?start='

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}


def fetch(session, page):
    with session.get(f'{url}{page * 25}', headers=headers) as r, open(f'top250-{page}.html', 'w') as f:
        f.write(r.text())


def main():
    with requests.Session() as session:
        for p in range(25):
            fetch(session, p)


# 多进程
def process_main():
    with Pool() as pool, requests.Session() as session:
        pool.starmap(fetch, [(session, p) for p in range(25)])


# 多线程
def thread_main():
    # 线程数量控制为 5 个
    with ThreadPool(processes=5) as pool, requests.Session() as session:
        pool.starmap(fetch, [(session, p) for p in range(25)])


# concurrent
def concurrent_main():
    with ThreadPoolExecutor(max_workers=5) as pool, requests.Session() as session:
        list(pool.map(partial(fetch, session), range(25)))


async def fetch_async(session, page):
    r = await session.get(f'{url}{page*25}', headers=headers)
    async with aiofiles.open(f'top250-{page}.html', mode='w') as f:
        await f.write(await r.text())


async def async_main():
    loop = asyncio.get_event_loop()
    async with aiohttp.ClientSession(loop=loop) as session:
        tasks = [asyncio.ensure_future(fetch(session, p)) for p in range(25)]
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    main()
    process_main()
    thread_main()
    concurrent_main()
    asyncio.run(async_main())
