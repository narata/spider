# -*- coding: utf-8 -*-
# @Time     : 2018/7/12 9:58
# @Author   : Narata
# @Project  : spider
# @File     : 1.py
# @Software : PyCharm


from urllib import request
from lxml import etree
import re


headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Referer': 'https://www.douban.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }


def run():
    url = 'https://www.xklxsw.com/book/38500/'
    req = request.Request(url)
    resp = request.urlopen(req)
    html = resp.read().decode('gbk')
    # print(html)
    test = etree.HTML(html)
    result = test.xpath("//div[@class='content']/div[5]/span/a/@href")
    for i in range(0, len(result)):
        try:
            buf = result[i]
            print(i)
            run1(url + buf)
        except:
            continue
        

def run1(url):
    req = request.Request(url)
    resp = request.urlopen(req)
    html = resp.read().decode('gbk')
    reg = r'<h1 class="title">章节目录 (.*?)</h1>'
    title = re.findall(reg, html, re.S)[0]
    reg = r'<b class="red">m.xklxsw.com</b>(.*?)<p>可乐小说网最快更新，无弹窗阅读请'
    text = re.findall(reg, html, re.S)[0].replace('<br />', '').replace('&nbsp;', '').replace(' ', '')
    with open('test/{}.txt'.format(title), 'w', encoding='gbk') as fp:
        fp.write(text)
    

run()