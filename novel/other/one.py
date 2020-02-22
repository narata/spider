import requests
from lxml import etree

r = requests.get('https://www.33yq.com/read/64931/#footer')
e = etree.HTML(r.content.decode('utf-8'))
names = e.xpath("//dd/a/text()")
urls = e.xpath("//dd/a/@href")
base_url = 'https://www.33yq.com'
for i in range(0, len(names)):
    url = base_url + urls[i]
    print(url)
    r1 = requests.get(url)
    e1 = etree.HTML(r1.content.decode('utf-8'))
    print(e1.xpath("//div[@class='context']/p/text()"))
    break
print(names)
print(urls)
