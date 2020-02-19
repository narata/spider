import requests

a = ["180.210.201.54:3128"]

try:
    r = requests.get('http://w2.h528.com/post/category/%e4%ba%ba%e5%a6%bb%e7%86%9f%e5%a5%b3/page/4',
                     proxies={"http": "173.212.216.52:3128"})
    print(r.text)
except:
    print('connect failed')
else:
    print('success')
