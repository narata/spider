import requests
from lxml import etree
from langconv import *
from fake_useragent import UserAgent
import os
import time

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_{0}) AppleWebKit/53{0}.36 (KHTML, like Gecko) Chrome/80.{0}.3987.106 Safari/53{0}.36'

path = "data/强暴虐待"

ua = UserAgent()

if not os.path.exists(path):
    os.makedirs(path)

for i in range(1, 32):
    url = "http://w2.h528.com/post/category/%e5%bc%b7%e6%9a%b4%e8%99%90%e5%be%85/page" + str(i)
    print(url)
    headers = {'User_Agent': ua.random}
    resp = requests.get(url, headers=headers)
    html = resp.content.decode('utf-8')
    test = etree.HTML(html)
    urls = test.xpath("//a[@rel='bookmark']/@href")
    names = test.xpath("//a[@rel='bookmark']/text()")
    for j in range(0, len(urls)):
        try:
            name = names[j].replace(' ', '').replace('/', '')
            name = Converter('zh-hans').convert(name)
            if os.path.exists(path + "/{}.txt".format(name)):
                print(i, j, name, "pass")
                continue
            headers = {'User_Agent': ua.random}
            resp = requests.get(urls[j], headers=headers)
            html_novel = resp.content.decode('utf-8')
            test_novel = etree.HTML(html_novel)
            text = test_novel.xpath("//p/text()")
            with open(path + "/{}.txt".format(name), "w") as fp:
                fp.write(Converter('zh-hans').convert("\n".join(text)))
            print(i, j, name)
        except UnicodeDecodeError as e:
            print(i, j, urls[j])
