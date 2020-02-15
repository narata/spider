from urllib import request
from lxml import etree
import re
import os

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Referer': 'https://www.xbookcn.net/book/abin/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

dir_name = "日译名家"
if not os.path.exists("data/" + dir_name):
    os.makedirs("data/" + dir_name)
url = "https://www.xbookcn.net/class/riyi.htm"
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
html = resp.read().decode('gbk')
test = etree.HTML(html)
novel_names = test.xpath("//a/text()")
novel_urls = test.xpath("//a/@href")
for i in range(0, len(novel_urls)):
    print(novel_urls[i], novel_names[i])
