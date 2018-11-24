# -*- coding: utf-8 -*-
# @Time     : 2018/5/3 22:04
# @Author   : Narata
# @Project  : spider
# @File     : first.py
# @Software : PyCharm

from urllib.request import ProxyHandler, build_opener
from urllib.error import URLError

url = 'http://www.ditecting.com'

proxy_handler = ProxyHandler({
    'http': 'http://127.0.0.1:9743'
})
opener = build_opener(proxy_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
