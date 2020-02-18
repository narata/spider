from urllib import request
from lxml import etree
import re
import os

headers = {
    'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    'Referer': 'http://w2.h528.com/post/category/%e4%ba%ba%e5%a6%bb%e7%86%9f%e5%a5%b3',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}
path = "data/人妻熟女"

if not os.path.exists(path):
    os.makedirs(path)

for i in range(1, 177):
    url = "http://w2.h528.com/post/category/%e4%ba%ba%e5%a6%bb%e7%86%9f%e5%a5%b3/page/" + str(i)
    req = request.Request(url, headers=headers)
    resp = request.urlopen(req)
    html = resp.read().decode('utf-8')
    test = etree.HTML(html)
    urls = test.xpath("//a[@rel='bookmark']/@href")
    names = test.xpath("//a[@rel='bookmark']/text()")
    for j in range(0, len(urls)):
        req_novel = request.Request(urls[j], headers=headers)
        resp_novel = request.urlopen(req_novel)
        html_novel = resp_novel.read().decode('utf-8')
        test_novel = etree.HTML(html_novel)
        text = test_novel.xpath("//p/text()")
        with open(path + "/{}.txt".format(names[j]), "w") as fp:
            fp.write("".join(text))
        print(names[j])