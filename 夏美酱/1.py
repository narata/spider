# -*- coding: utf-8 -*-
# @Time     : 2018/11/24 20:39
# @Author   : Narata
# @Project  : spider
# @File     : 1.py
# @Software : PyCharm


from urllib import request
from lxml import etree
import re
import os


headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Referer': 'https://www.douban.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }


def run():
    url = 'https://www.meituri.com/t/298/'
    req = request.Request(url)
    resp = request.urlopen(req)
    html = resp.read()
    # print(html)
    test = etree.HTML(html)
    result1 = test.xpath("//div[@class='hezi']/ul[1]/li/p[3]/a/@href")
    result2 = test.xpath("//div[@class='hezi']/ul[1]/li/p[3]/a/text()")
    num = test.xpath("//div[@class='hezi']/ul[1]/li/span/text()")
    # print(result)
    for i in range(0, len(result1)):
        try:
            buf1 = result1[i]
            buf2 = result2[i]
            buf3 = int(num[i][:-1])
            if not os.path.exists("./data/" + buf2):
                os.makedirs("./data/" + buf2)
            print(i)
            run1(i, buf1, buf2, buf3)
            break
        except:
            continue


def run1(i, buf1, buf2, buf3):
    for i in range(1, buf3+1):
        url = "https://ii.hywly.com/a/1/" + buf1.split('/')[-2] + "/" + "{}.jpg".format(i)
        data = request.urlopen(url).read()
        path = "./data/" + buf2 + '/{}.jpg'.format(i)
        with open(path, 'wb') as file:
            file.write(data)
        print(i, url)
     
        
run()
