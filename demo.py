# -*- coding: utf-8 -*-
# @Time    : 2018/4/10 下午11:12
# @Author  : Narata
# @File    : demo.py
# @Software: PyCharm


from urllib import request, error, parse

try:
    headers = {
        'User_Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/65.0.3325.181 Safari/537.36'
    }
    data = {
        'source': 'index_nav',
        'form_email': '13940218231',
        'form_password': 'jt09101025'
    }
    data = parse.urlencode(data).encode('utf8')
    url = 'https://www.douban.com/accounts/login'
    response = request.Request(url, headers=headers, data=data)
    html = request.urlopen(response)
    result = html.read().decode('utf8')
    print(result)
except error.URLError as e:
    if hasattr(e, 'reason'):
        print('错误原因是' + str(e.reason))
except error.HTTPError as e:
    if hasattr(e, 'code'):
        print('错误状态码是' + str(e.code))
else:
    print('请求成功通过。')
