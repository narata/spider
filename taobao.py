# coding: utf8
# Create by Narata on 2018/4/10

import time
import requests
import re
import json
from hashlib import md5

t = time.localtime()
find_arg = {
    'q': 'python',
    'initiative_id': 'staobaoz_{}{:0>2d}{:0>2d}'.format(t[0], t[1], t[2])
}
print(find_arg)
first_url = 'https://s.taobao.com/search?imgfile=&js=1&stats_click=search_radio_all%3A1&ie=utf8'

r = requests.get(first_url, params=find_arg)
html = r.text
# print(html)/

reg = r'g_page_config = (.*?);\n    g_srp_loadCss'
content = re.findall(reg, html, re.S)[0]
content = json.loads(content)
data_list = content['mods']['itemlist']['data']['auctions']
# for buf in data_list:
#     print(buf['raw_title'])
print(len(data_list))

cookie = r.cookies
print(cookie)

ksts = str(int(time.time()*1000))
print()
print(ksts)

second_url = \
    'https://s.taobao.com/api?_ksTS={}_222&callback=jsonp223&ajax=true&m=customized&sourceId=tb.index&q=python' \
    '&spm=a21bo.2017.201856-taobao-item.1&s=36&imgfile=&initiative_id=tbindexz_20170306&bcoffset=-1&commend=all' \
    '&ie=utf8&rn={}&ssid=s5-e&search_type=item'.format(ksts, md5(ksts.encode()).hexdigest())

r2 = requests.get(second_url, params=find_arg, cookies=cookie)
html = r2.text
data_list = json.loads(re.findall(r'{.*}', html)[0])['API.CustomizedApi']['itemlist']['auctions']
for buf in data_list:
    print(buf['raw_title'])
print(data_list)

# with open('taobao.html', 'w', encoding='utf8') as fp:
#     fp.write(html)
