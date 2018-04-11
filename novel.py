# -*- coding: utf-8 -*-
# @Time     : 2018/4/11 10:26
# @Author   : Shark
# @File     : novel.py
# @Software : PyCharm

from urllib import request
import re
import pymysql


class Sql(object):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='narata',
        db='novel',
        charset='utf8'
    )
    
    def add_novel(self, sort, sort_name, book_name, img_url, description, status, author):
        cur = self.conn.cursor()
        cur.execute("insert into novel(sort, sortname, bookname, imgurl, description, status, author) values({}, '{}', '{}', '{}', '{}', '{}', '{}')".format(sort, sort_name, book_name, img_url, description, status, author))
        lastrowid = cur.lastrowid
        cur.close()
        self.conn.commit()
        return lastrowid
    
    def add_chapter(self, novel_id, title, content):
        cur = self.conn.cursor()
        cur.execute("insert into chapter(novelid, title, content) values({}, '{}', '{}')".format(novel_id, title, content))
        cur.close()
        self.conn.commit()
        

mysql = Sql()


sort_dict = {
    1: '玄幻魔法',
    2: '武侠修真',
    3: '纯爱耽美',
    4: '都市言情',
    5: '职场校园',
    6: '穿越重生',
    7: '历史军事',
    8: '网游动漫',
    9: '恐怖灵异',
    10: '科幻小说',
    11: '美文名著',
}


def get_chapter_content(url):
    response = request.urlopen(url)
    html = response.read().decode('GBK')
    reg = r'style5\(\);</script>(.*?)style6\(\);'
    html = re.findall(reg, html, re.S)[0]
    return html


def get_chapter_list(url, novel_id):
    response = request.urlopen(url)
    html = response.read().decode('GBK')
    reg = r'<li><a href="(.*?)" title=".*?">(.*?)</a></li>'
    chapter_info = re.findall(reg, html)
    for url, title in chapter_info:
        content = get_chapter_content(url)
        mysql.add_chapter(novel_id, title, content)
        break


def get_novel(url, sort_id, sort_name):
    response = request.urlopen(url)
    html = response.read().decode('GBK')
    book_name = re.findall(r'<meta property="og:novel:book_name" content="(.*?)"/>', html)[0]
    description = re.findall(r'<meta property="og:description" content="(.*?)"/>', html, re.S)[0]
    img_url = re.findall(r'<meta property="og:image" content="(.*?)"/>', html)[0]
    author = re.findall(r'<meta property="og:novel:author" content="(.*?)"/>', html)[0]
    status = re.findall(r'<meta property="og:novel:status" content="(.*?)"/>', html)[0]
    chapter_url = re.findall(r'<a href="(.*?)" class="reader"', html)[0]
    print(book_name, img_url, author, status, chapter_url)
    novel_id = mysql.add_novel(sort_id, sort_name, book_name, img_url, description, status, author)
    get_chapter_list(chapter_url, novel_id)


def get_list(sort_id, sort_name):
    url = 'http://www.quanshuwang.com/list/{}_1.html'.format(sort_id)
    response = request.urlopen(url)
    reg = r'<a target="_blank" href="(.*?)" class="l mr10">'
    url_list = re.findall(reg, response.read().decode('GBK'))
    for url in url_list:
        get_novel(url, sort_id, sort_name)
        break


for sort_id, sort_name in sort_dict.items():
    get_list(sort_id, sort_name)