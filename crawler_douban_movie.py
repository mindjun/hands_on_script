#!/usr/bin/env python
# encoding=utf-8

"""
爬取豆瓣电影TOP250 - 完整示例代码
"""

import codecs
import time
import requests
from bs4 import BeautifulSoup

DOWNLOAD_URL = 'http://movie.douban.com/top250/'


def download_page(url):
    return requests.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }).content


def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    movie_list_soup = soup.find('ol', attrs={'class': 'grid_view'})

    movie_name_list = []
    if movie_list_soup:
        for movie_li in movie_list_soup.find_all('li'):
            detail = movie_li.find('div', attrs={'class': 'hd'})
            movie_name = detail.find('span', attrs={'class': 'title'}).getText()
            movie_name_list.append(movie_name)
            movie_detail = detail.find('a', attrs={'class': ''})['href']
            if movie_detail:
                detail = download_page(movie_detail)
                detail = BeautifulSoup(detail, "html.parser")
                detail_div = detail.find('div', attrs={'id': 'link-report'})
                try:
                    detail_span = detail_div.find('span', attrs={'property': 'v:summary'}).getText()
                    movie_name_list.append(detail_span.strip())
                except Exception as ex:
                    print(Exception)
                    print(type(ex))
        next_page = soup.find('span', attrs={'class': 'next'}).find('a')
        if next_page:
            return movie_name_list, DOWNLOAD_URL + next_page['href']
        return movie_name_list, None
    else:
        print(soup)
        return 'error', None


def main():
    url = DOWNLOAD_URL

    with codecs.open('movies', 'wb', encoding='utf-8') as fp:
        while url:
            time.sleep(2)
            html = download_page(url)
            movies, url = parse_html(html)
            fp.write(u'{movies}\n'.format(movies='\n'.join(movies)))


if __name__ == '__main__':
    main()
