#urllib是一个python包,含有四个模块,主要通过request与网页相连,通过urlopen打开
import urllib.request

response = urllib.request.urlopen('http://placekitten.com/g/500/600')
cat_img = response.read()

with open('cat_500_600.jpg', 'wb') as f:
    f.write(cat_img)

#geturl得到链接地址
response.geturl()
#info得到httpmessage对象
response.info()
print(response.info())
#getcode得到http状态
response.getcode()