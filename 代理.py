#有些时候爬很多图片or数据时会被kill,使用代理可以让服务器看到的是代理服务器而不是我们自己的地址,可以避免被kill
#1.参数是一个字典{'类型':'代理ip:端口号'}：proxy_support=urllib.resquest.ProxyHandler({})
#2.定制、创建一个opener：opener=urllib.resquest.build_opener(proxy_support)
#3.安装opener:urllib.resquest.install_opener(opener)
#4.调用opener：opener.open(url)

import urllib.request
import random

#测试目前ip地址
url = 'http://www.whatismyip.com.tw'

iplist = ['101.231.104.82:80', '119.41.236.180:8010', '183.146.213.157:80', '39.105.229.239:8080']

proxy_support = urllib.request.ProxyHandler({'http': random.choice(iplist)})
opener = urllib.request.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')]
urllib.request.install_opener(opener)
response = urllib.request.urlopen(url)
html = response.read().decode('utf-8')
print(html)