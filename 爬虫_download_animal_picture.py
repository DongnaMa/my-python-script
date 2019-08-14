#爬取10页网页上的动物图片
#os创建文件夹

import urllib.request
import os
import re

def url_open(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.65 Safari/537.36')
    response = urllib.request.urlopen(url)
    html = response.read()
    return html

def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]

def find_imgs(url):
    html = url_open(url).decode('utf-8')
    reg = r"//[0-9a-z]+\.sinaimg\.cn.*?\.jpg"
    img = re.compile(reg)
    img_address = re.findall(img, html)
    return img_address

def save_imgs(folder, img_address):
    for each in img_address:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open('https:'+each)
            f.write(img)

def download_animal(folder='so_cute', pages=3):
    os.mkdir(folder)
    os.chdir(folder)
    url = 'http://jandan.net/zoo/'
    page_num = int(get_page(url))
    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_address = find_imgs(page_url)
        save_imgs(folder, img_address)


if __name__ == '__main__':
    download_animal()