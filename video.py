# coding: utf8
# Create by Narata on 2018/4/10

import urllib.request
import re


def get_url_list():
    url = 'http://www.budejie.com/video/'
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36')
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf8')
    print(type(html))
    reg = r'data-mp4="(.*?)"'
    url_list = re.findall(reg, html)
    for url in url_list:
        urllib.request.urlretrieve(url, 'mp4/{}.mp4'.format(url.split('/')[-1].split('.')[0]))
        print(url)


get_url_list()