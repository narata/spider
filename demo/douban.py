# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 下午11:12
# @Author  : Narata
# @File    : demo.py
# @Software: PyCharm


from urllib import request, error, parse
import http.cookiejar
import re
from matplotlib import pyplot, image
import json

headers = {
        'User_Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
        'Referer': 'https://www.douban.com/',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        }

# cookie
cj = http.cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cj))


def login():
    try:
        data = {
            'source': 'index_nav',
            'form_email': '',
            'form_password': ''
        }
    
        # 第一次连接，为了获得cookie
        url_1 = 'https://www.douban.com'
        response_1 = request.Request(url_1, headers=headers)
        html_1 = opener.open(response_1)
        
        # 获取验证码
        text = html_1.read().decode('utf8')
        if '验证码' in text:
            reg = r'name="captcha-id" value="(.*?)"/>.*?id="captcha_image" src="(.*?)" alt="captcha" class="captcha_image"'
            captcha_id, captcha_url = re.findall(reg, text, re.S)[0]
            # 存储验证码
            request.urlretrieve(captcha_url, 'picture/captcha.jpg')
            pyplot.imshow(image.imread('picture/captcha.jpg'))
            pyplot.axis('off')
            pyplot.show()
            
            # 输入验证码
            captcha_solution = input('请输入验证码：')
        
            # 补充data
            data['captcha-solution'] = captcha_solution
            data['captcha-id'] = captcha_id
        
        # 第二次连接，登录
        url_2 = 'https://www.douban.com/accounts/login'
        response_2 = request.Request(url_2, headers=headers, data=parse.urlencode(data).encode('utf8'))
        html_2 = opener.open(response_2)
        text = html_2.read().decode('utf8')
        if '登录豆瓣' not in text:
            return True
        else:
            return False
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print('错误原因是' + str(e.reason))
    except error.HTTPError as e:
        if hasattr(e, 'code'):
            print('错误状态码是' + str(e.code))
            
            
url = 'https://movie.douban.com/j/new_search_subjects?sort=T&range=0,10&tags={}&start={}&genres'

forms = '电影'
types = '剧情'

tags = request.quote(forms) + ',' + request.quote(types)
for i in range(0, 1000, 20):
    url_buf = url.format(tags, i)
    response = request.Request(url_buf, headers=headers)
    html = opener.open(response)
    data = json.loads(html.read().decode('utf8'))
    for buf in data['data']:
        print(buf['title'], buf['rate'])

# if __name__ == '__main__':
#     print(login())