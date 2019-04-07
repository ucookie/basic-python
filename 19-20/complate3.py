#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import csv
import time
import requests
from requests.exceptions import RequestException
from lxml import etree

def download_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36'}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            print('状态码：', response.status_code)
            return None
    except RequestException:
        print('请求错误')
        return None

def parse_data(html):
    '''解析数据'''
    movies = list()
    html = etree.HTML(html)
    item = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for x in item:
        movies.append(
            (
                x.xpath('./i/text()')[0],
                x.xpath('./a/img[2]/@data-src')[0].split('@')[0],
                x.xpath('./a/@title')[0],
                x.xpath('.//p[@class = "star"]/text()')[0].strip().split('：')[1],
                get_release_time(x.xpath('.//p[@class = "releasetime"]/text()')[0].strip()[5:]),
                get_release_area(x.xpath('.//p[@class = "releasetime"]/text()')[0].strip()[5:]),
                x.xpath('.//p[@class = "score"]/i[1]/text()')[0] + x.xpath('.//p[@class = "score"]/i[2]/text()')[0]
            )
        )
    return movies

def save_data(movies):
    '''保存数据'''
    with open('猫眼top100.csv', 'a', encoding='utf-8', newline='') as fobj:
        csv_obj = csv.writer(fobj)
        for line in movies:
            csv_obj.writerow(line)

def save_img(url, name):
    '''保存图片'''
    try:
        response = requests.get(url)
        # 图片需要使用二进制格式
        with open('cover/' + name + '.jpg', 'wb') as f:
            f.write(response.content)
    except RequestException as ex:
        print('保存出错:', str(ex))
        pass

# ============================================================
# 内部函数
# ============================================================
def get_release_time(data):
    '''提取时间函数'''
    pattern = re.compile(r'(.*?)(\(|$)')
    items = re.search(pattern, data)
    if items is None:
        return '未知'
    # 返回匹配到的第一个括号(.*?)中结果即时间
    return items.group(1)

def get_release_area(data):
    '''提取国家/地区函数'''
    pattern = re.compile(r'.*\((.*)\)')

    items = re.search(pattern, data)
    if items is None:
        return '未知'
    # $表示匹配一行字符串的结尾，这里就是(.*?)；\(|$,表示匹配字符串含有(,或者只有(.*?)
    return items.group(1)

def main():
    for i in range(0, 10):
        url = 'https://maoyan.com/board/4?offset=%s' % (i*10)
        html = download_page(url)
        movies = parse_data(html)
        # 调试
        for x in movies: print(x)

        # save_data(movies)
        # for movie in movies:
        #     save_img(movie[1], movie[2])

        # 防止访问过快,被禁止
        time.sleep(0.5)

if __name__ == "__main__":
    main()