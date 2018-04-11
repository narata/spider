# -*- coding: utf-8 -*-
# @Time     : 2018/4/11 16:14
# @Author   : Shark
# @File     : verification_code.py
# @Software : PyCharm

from aip import AipOcr

APP_ID = '10769158'
API_KEY = 'C2Uo8OGGY1O1RVwGOkrb68it'
SECRET_KEY = '1ldb72IgGBVhrmrjtC3jTi8iyWnU70OM'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


# 读取图片
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
    
    
# options = {}
# options["language_type"] = "ENG"

image = get_file_content('picture/captcha.jpg')

url = 'https://www.douban.com/misc/captcha?id=U5ivIQP8K6C4lUTSJY9DaeJg:en&amp;size=s'


print(client.basicGeneralUrl(url))

