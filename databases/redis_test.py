# -*- coding: utf-8 -*-
# @Time     : 2018/5/5 20:21
# @Author   : Narata
# @Project  : spider
# @File     : redis_test.py
# @Software : PyCharm


from redis import StrictRedis

redis = StrictRedis(host='localhost', port=6379, db=0)
redis.set('name', 'Bob')
print(redis.get('name'))
