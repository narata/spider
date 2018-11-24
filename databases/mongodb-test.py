# -*- coding: utf-8 -*-
# @Time     : 2018/5/5 21:19
# @Author   : Narata
# @Project  : spider
# @File     : mongodb-test.py
# @Software : PyCharm

import pymongo

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.test
collection = db.students


def insert():
    student = {
        'id': '4',
        'name': 'narata',
        'age': '25',
        'gender': 'male'
    }
    result = collection.insert(student)
    print(result)
    

def find():
    result = collection.find({'name': 'narata'})
    print(type(result))
    print(result[0])
    
    
if __name__ == '__main__':
    find()
