#urlopen(url, data, head),url:需要打开的网址;data:Post提交的数据;head:隐藏python代码,防治被kill
#json.loads:将已编码的JSON字符串解码为Python对象

import urllib.request
import urllib.parse
import json

content = input('请输出需要翻译的内容：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/'
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36'

data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'anyi.web'
data['ue'] = 'UTF-8'
data['typeResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

response = urllib.request.urlopen(url, data, head)
html = response.read().decode('utf-8')

target = json.loads(html)
print('翻译结果：%s' % (target['translateResult'][0][0]['tgt']))
