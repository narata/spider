# -*- coding: utf-8 -*-
# @Time     : 2018/7/12 10:59
# @Author   : Narata
# @Project  : spider
# @File     : 2.py
# @Software : PyCharm


import os
import re
result = os.listdir('test')
buf = sorted(result, key=lambda x: int(re.findall(r'第(.*?)章', x)[0]))
with open('乡野风月.txt', 'w') as fp:
    for file in buf:
        with open('test/{}'.format(file), 'r') as fp1:
            fp.write(file + '\n')
            fp.write(fp1.read().replace('\n\n\n', '\n'))
            fp.write('\n\n\n----------------------------------------------------------------------------------------------\n\n\n')
