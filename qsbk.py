# -*- coding: utf-8 -*-
# @Time     : 2018/4/11 13:17
# @Author   : Shark
# @File     : qsbk.py
# @Software : PyCharm

from lxml import html
import requests
import threading
from queue import Queue


class CrawlThread(threading.Thread):
    
    def __init__(self, thread_id, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.queue = queue
        
    def run(self):
        print('run')
    


