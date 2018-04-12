# -*- coding: utf-8 -*-
# @Time     : 2018/4/12 15:35
# @Author   : Shark
# @File     : doutu.py
# @Software : PyCharm

import scrapy
from ..items import DoutuItem
import os
import requests


class DouTu(scrapy.Spider):
    name = 'doutu'
    allowed_domains = ['doutula.com']
    start_urls = [
        'http://www.doutula.com/photo/list/?page={}'.format(i) for i in range(1, 2)
    ]
    
    def parse(self, response):
        p = response.xpath('//div[@class="page-content text-center"]/div/a/img[contains(@class, "img-responsive")]')
        items = DoutuItem()
        items['image_urls'] = []
        for content in p:
            items['image_urls'].append(content.xpath('./@data-original').extract_first())
            # items['name'] = content.xpath('./@alt').extract_first()
            
            # try:
            #     file_name = 'picture/{}.{}'.format(items['name'], items['image_urls'].split('.')[-1])
            #     if not os.path.exists(file_name):
            #         r = requests.get(items['image_urls'])
            #         with open(file_name, 'wb') as fp:
            #             fp.write(r.content)
            # except Exception as e:
            #     print(e)
        print(items['image_urls'])
        yield items
