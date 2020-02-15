# -*- coding: utf-8 -*-
# @Time    : 2019-02-16 18:02
# @Author  : Narata
# @File    : test.py
# @Software: PyCharm

from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

url = 'https://blog.csdn.net/narata1/article/details/87361376'

proxy_handler = ProxyHandler({
    'http': '116.209.57.227:9999'
})
opener = build_opener(proxy_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)