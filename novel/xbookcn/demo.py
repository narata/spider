from urllib import request
from lxml import etree
import re

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Referer': 'https://www.xbookcn.net/book/abin/',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

for i in range(62, 999):
    try:
        url = 'https://www.xbookcn.net/read/story'+str(i).zfill(3)+'.htm'
        print(url)
        req = request.Request(url, headers=headers)
        resp = request.urlopen(req)
        html = resp.read().decode('gbk')
        # print(html)
        test = etree.HTML(html)
        header = test.xpath("//h3/text()")[0]
        text = test.xpath("//p/text()")
        with open("data/" + header + ".txt", "w") as fp:
            fp.write("".join(text))
        print(header)
    except Exception as e:
        print(e.message)

