# -*- coding: utf-8 -*-
# @Time     : 2018/4/13 9:15
# @Author   : Narata
# @File     : api_chinaz.py
# @Software : PyCharm
# @name     : 站长之家接口
# @function : 返回ip对应的域名，以及位置信息
# @version  : Python3.6


from urllib import request, parse
import random
import re


class ChinaZApi:
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:59.0) Gecko/20100101 Firefox/59.0',
    }
    url = 'http://ip.chinaz.com/ajaxsync.aspx?at=ipbatch&callback=jQuery{}'.format(random.random())
    
    @staticmethod
    def get_ip_address(ip):
        data = {
            'ip': ip
        }
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url=ChinaZApi.url, headers=ChinaZApi.headers, data=data)
        response = request.urlopen(req)
        result = response.read().decode('utf8')
        reg = r"'(.*?)'"
        result = re.findall(reg, result)
        return {
            'ip': result[1],
            'domain': result[0],
            'address': result[3]
        }
        
        
if __name__ == '__main__':
    print(ChinaZApi.get_ip_address('1.1.1.1'))
