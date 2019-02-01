# -*- coding: utf-8 -*-
# @Time     : 2018/11/24 20:39
# @Author   : Narata
# @Project  : spider
# @File     : 1.py
# @Software : PyCharm


from urllib import request
from lxml import etree
import os
import sys
import threading
import queue

queueLock = threading.Lock()
workQueue = queue.Queue()
exitFlag = 0


class MyThread (threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while not exitFlag:
            url, path = self.queue.get()
            data = request.urlopen(url).read()
            with open(path, 'wb') as file:
                file.write(data)
            print(url)


headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Referer': 'https://www.douban.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }



def run(url):
    # url = 'https://www.meituri.com/t/2196/'
    req = request.Request(url)
    resp = request.urlopen(req)
    html = resp.read()
    # print(html)
    test = etree.HTML(html)
    result1 = test.xpath("//div[@class='hezi']/ul[1]/li/p[3]/a/@href")
    result2 = test.xpath("//div[@class='hezi']/ul[1]/li/p[3]/a/text()")
    num = test.xpath("//div[@class='hezi']/ul[1]/li/span/text()")
    name = test.xpath("//title/text()")[0].split('-')[0].replace('|', '').replace(' ', '')
    print(name)
    # exit(1)
    # print(result)
    for i in range(0, len(result1)):
        buf1 = result1[i]
        buf2 = result2[i]
        buf3 = int(num[i][:-1])
        if not os.path.exists("./data/{}/".format(name) + buf2):
            os.makedirs("./data/{}/".format(name) + buf2)
        print(i, buf3 )
        run1(buf1, buf2, buf3, name)


def run1(buf1, buf2, buf3, name):
    for i in range(0, buf3+1):
        try:
            url = "https://ii.hywly.com/a/1/" + buf1.split('/')[-2] + "/" + "{}.jpg".format(i)
            path = "./data/{}/".format(name) + buf2 + '/{}.jpg'.format(i)
            workQueue.put([url, path])
            print(url)
        except Exception as e:
            print(e)


run(sys.argv[1])
threads = []
for i in range(10):
    thread = MyThread(workQueue)
    thread.start()
    threads.append(thread)
while not workQueue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()
