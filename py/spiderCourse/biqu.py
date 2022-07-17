# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import urllib.response
import urllib3
import sys
"""
类说明:下载《笔趣看》网小说《一念永恒》
Parameters:
    无
Returns:
    无
Modify:
    2022-09-13
"""
class Biqu(object):
    def __init__(self):
        self.server = 'http://www.biqukan.com/'
        self.target = 'http://www.biqukan.com/1_1094/'
        #存放章节名
        self.names = [] 
        #存放章节链接           
        self.urls = []            
        self.nums = 0

    def getTarget(self):
        target = 'https://www.bqkan8.com/74_74443/537021862.html'
        req = requests.get(url=target)
        htm = req.text
        bf  = BeautifulSoup(htm)
        texts = bf.find_all('div',class_ = 'showtxt')
        # 剔除空格，替换回车进行分段
        cont = texts[0].text.replace('\xa0','\n\n')
        print(cont)

    def getAll(self):
        server = 'http://www.biqukan.com/'
        target = 'https://www.bqkan8.com/74_74443/'
        req = requests.get(url = target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')

        print(str(div[0]))
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        for each in a:
          print(each.string, server + each.get('href'))

    """
    函数说明:获取下载链接
    Parameters:
        无
    Returns:
        无
    Modify:
        2022-09-13
    """
    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.text
        div_bf = BeautifulSoup(html)
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]))
        a = a_bf.find_all('a')
        self.nums = len(a[13:])                                #剔除不必要的章节，并统计章节数
        for each in a[13:]:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    """
    函数说明:获取章节内容
    Parameters:
        target - 下载连接(string)
    Returns:
        texts - 章节内容(string)
    Modify:
        2022-09-13
    """
    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.text
        bf = BeautifulSoup(html)
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    """
    函数说明:将爬取的文章内容写入文件
    Parameters:
        name - 章节名称(string)
        path - 当前路径下,小说保存名称(string)
        text - 章节内容(string)
    Returns:
        无
    Modify:
        2022-09-13
    """
    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')
 

if __name__ == '__main__':

    dl = Biqu()
    dl.get_download_url()
    print('《一年永恒》开始下载：')
    for i in range(5):
        dl.writer(dl.names[i], 'D:\一念永恒.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write("  已下载:%.3f%%" %  float(i/dl.nums) + '\r')
        sys.stdout.flush()
    print('《一年永恒》下载完成')
    # header = {
    #   "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    # }
    # res = urllib.request.Request(target,headers=header)
    # #print(res.status)
    # #print(res.data.decode())
    # resp = urllib.request.urlopen(res)
    # html = resp.read()
    # print(html)