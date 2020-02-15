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

url = "https://www.xbookcn.net/read/"
req = request.Request(url, headers=headers)
resp = request.urlopen(req)
html = resp.read().decode('gbk')
test = etree.HTML(html)
class_names = test.xpath("//a/text()")
class_urls = test.xpath("//a/@href")
for i in range(0, 17):
    if not os.path.exists("data/{}".format(class_names[i])):
        os.makedirs("data/{}".format(class_names[i]))
    class_url = "https://www.xbookcn.net/read/" + class_urls[i]
    req_class = request.Request(class_url, headers=headers)
    resp_class = request.urlopen(req)
    html_class = resp_class.read().decode('gbk')
    test_class = etree.HTML(html_class)
    novel_urls = test_class.xpath("//a/@href")
    novel_names = test_class.xpath("//a/text()")
    for j in range(0, len(novel_urls)):
        if "story" in novel_urls[j]:
            try:
                novel_url = "https://www.xbookcn.net/read/" + novel_urls[j]
                req_novel = request.Request(class_url, headers=headers)
                resp_novel = request.urlopen(req)
                html_novel = resp_novel.read().decode('gbk')
                test_novel = etree.HTML(html_novel)
                text = test.xpath("//p/text()")
                with open("data/{}/{}.txt".format(class_names[i], novel_names[j]), "w") as fp:
                    fp.write("".join(text))
                print(class_names[i], novel_names[j])
            except Exception as e:
                print(e.message)
