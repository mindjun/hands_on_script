# -*- coding:utf-8 -*-
import asyncio
from time import time

import aiohttp
from lxml import etree

url_ = 'https://movie.douban.com/top250'


# 通过 async 定义的函数叫做 coroutine ，即协程对象
async def fetch_content(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # await 是一个协程，不会阻塞，立即返回，返回的是协程对象
            # await 的时候，就会让出控制权，以便 loop 调用协程
            return await response.text()


async def parse(url):
    page = await fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)

    fetch_list = []
    result = []

    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))
    print(fetch_list)
    tasks = [fetch_content(url) for url in fetch_list]
    pages = await asyncio.gather(*tasks)

    for page in pages:
        html = etree.HTML(page)
        for element_movie in html.xpath(xpath_movie):
            result.append(element_movie)

    title_list = list()
    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
        # print(i, title)
        title_list.append((i, title))
    print(title_list)


def main():
    # 定义一个事件循环
    loop = asyncio.get_event_loop()
    start = time()
    for i in range(2):
        # 阻塞调用，直到协程运行结束时才返回,参数是一个 future
        # 将协程加入到事件循环中
        # 协程对象不能直接运行，在注册事件循环的时候，
        # 其实是run_until_complete方法将协程包装成为了一个任务（task）对象.
        # task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果
        loop.run_until_complete(parse(url_))
    end = time()
    print(f'Cost {(end - start) / 5} seconds')
    loop.close()


main()
