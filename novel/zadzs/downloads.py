# -*- coding: utf-8 -*-
# @Time    : 2019-02-01 13:33
# @Author  : Narata
# @File    : downloads.py
# @Software: PyCharm


from urllib import request
from lxml import etree
import os
import re


headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Referer': 'https://www.douban.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }


def run():
    site = "http://www.zadzs.com"
    req = request.Request(site)
    resp = request.urlopen(req)
    html = resp.read().decode('utf-8')
    test = etree.HTML(html)
    classification_urls = test.xpath("//div[@class='category']/div[1]/p/a/@href")
    classification_names = test.xpath("//div[@class='category']/div[1]/p/a/text()")
    # print(classification_names)
    for i in range(0, len(classification_urls)):
        classification_url = site + classification_urls[i]
        classification_name = classification_names[i]
        if not os.path.exists("./data/{}".format(classification_name)):
            os.makedirs("./data/{}".format(classification_name))
        while classification_url:
            print(classification_url)
            req_class = request.Request(classification_url)
            resp_class = request.urlopen(req_class)
            html_class = resp_class.read().decode('utf-8')

            book_urls = etree.HTML(html_class).xpath("//div[@class='book-name']/a/@href")
            for book_url in book_urls:
                try:
                    req_book = request.Request(site + book_url)
                    resp_book = request.urlopen(req_book)
                    html_book = resp_book.read().decode('utf-8')
                    lxml_book = etree.HTML(html_book)
                    book_name = lxml_book.xpath("//div[@class='f-fl']/h3/@title")[0].replace("/", " ")
                    book_download_url = site + lxml_book.xpath("//div[@class='ops']/a/@href")[0]

                    req_book_download = request.Request(book_download_url)
                    resp_book_download = request.urlopen(req_book_download)
                    html_book_download = resp_book_download.read().decode('utf-8')

                    book_download_url_true = site + etree.HTML(html_book_download).xpath("//div[@class='panel-body']/a[1]/@href")[0]

                    if not os.path.exists("./data/{}/{}/".format(classification_name, book_name)):
                        os.makedirs("./data/{}/{}/".format(classification_name, book_name))
                    else:
                        break

                    req_book_text = request.Request(book_download_url_true)
                    resp_book_text = request.urlopen(req_book_text)
                    html_book_text = resp_book_text.read()

                    with open("./data/{}/{}/{}.txt".format(classification_name, book_name, book_name), "wb") as fp:
                        fp.write(html_book_text)

                    print(book_download_url_true)
                except:
                    pass
            print(book_urls)

            if "下一页" in html_class:
                classification_url = site + classification_urls[i] + etree.HTML(html_class).xpath("//span[@class='nums']/li/a[text()='下一页']/@href")[0]
            else:
                classification_url = None


if __name__ == '__main__':
    run()
