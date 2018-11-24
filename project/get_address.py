# -*- coding: utf-8 -*-
# @Time     : 2018/4/13 9:55
# @Author   : Narata
# @File     : get_address.py
# @Software : PyCharm

from project.api.api_chinaz import ChinaZApi
import threading
from queue import Queue


class GetAddressThread(threading.Thread):
    
    def __init__(self, queue, fp2):
        threading.Thread.__init__(self)
        self.queue = queue
        self.fp2 = fp2
        
    def run(self):
        while True:
            print('==========================')
            ip = self.queue.get()
            result = ChinaZApi.get_ip_address(ip)
            print(result)
            self.fp2.write(result['ip'] + ',' + result['domain'] + ',' + result['address'] + '\n')
            self.queue.task_done()
            
            
def main():
    with open('ip_102.csv', 'r') as fp1:
        with open('ip_102_result.csv', 'w') as fp2:
        #     queue = Queue(10)
        #     for i in range(5):
        #         w = GetAddressThread(queue, fp2)
        #         w.setDaemon(True)
        #         w.start()
        #     data = fp1.readlines()
        #     for ip in data:
        #         ip = ip.replace('\n', '')
        #         print(ip)
        #         queue.put(ip)
        #     queue.join()
            i = 0
            for ip in fp1.readlines():
                i += 1
                print(i)
                ip = ip.replace('\n', '')
                result = ChinaZApi.get_ip_address(ip)
                fp2.write(result['ip'] + ',' + result['domain'] + ',' + result['address'] + '\n')
                

def main_async():
    pass


main()
