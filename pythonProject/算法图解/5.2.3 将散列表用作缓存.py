# coding=utf-8
# Author:D.辉
# Place：哈工深
# Time：2021/11/21 10:15

cache = {}


def get_data_from_server(url):
    pass


def get_page(url):
    if cache.get(url):
        return cache[url]  # 返回缓存数据
    else:
        data = get_data_from_server(url)  # 先将数据保存到缓存中
        cache[url] = data
        return data


get_page("kongdehui")
get_page("kongdehui")
