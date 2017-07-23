#coding:utf-8
import urllib
import codecs #编解码器注册表和基类
import requests
from bs4 import BeautifulSoup 


######
def download_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    data = requests.get(url, headers=headers).content
    return data

#公司名称
def Co_name(html):
    soup = BeautifulSoup(html, 'html.parser')
    # 从上面的数据获取html文档并解析，这里使用的是Python自带的HTML解释器
    article = soup.find('div', attrs={'class': 'new-c3 f18 overflow-width'})   
    #article1 = article.find('div', attrs={'class': 'baseinfo-module-content-value'})
    # 缩小HTML文档的解析范围，限定在文章主体内部。获取文章主体内部标签内的文本
    name = article.find('span').getText() 
    # 获取文章主体内部的标签内的文本，可以获得相关内容。
    return name
    # 返回数据，用于写入文件。

def get_article(url):
    #file_name = title + '.txt'

    file_name = "/Users/Zyfx/Desktop/spider/zfx.txt"
    with codecs.open(file_name, 'wb', encoding='utf-8') as fp:
    	html= download_page(url)
    # 调用函数获取数据
    	name01 = Co_name(html)
    	fp.write(name01)
        # 将获取的数据写入文件。
        
    print('读取完毕！')
    return 'OK'

if __name__ == '__main__':
    url = 'http://www.tianyancha.com/company/22822'
    #title = 'zfx11'
    get_article(url)


