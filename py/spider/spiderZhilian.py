import urllib
import urllib.request
import urllib.response
import urllib3

import re


class zhiLian():
  def spider(self,position,workPlace):
    '''
    爬虫的主调度器
    :param position: 职位
    :param workPlace: 工作地点
    '''
    url="http://sou.zhaopin.com/jobs/searchresult.ashx?"
    url+=urllib.parse.urlencode({"kw":workPlace})
    url+="&"
    url+=urllib.parse.urlencode({"jl":position})
    isflow=True#是否进行下一页的爬去
    page=1
    http = urllib3.PoolManager(retries=2,timeout=10,num_pools=200,maxsize=200)
    while isflow:
      url+="&"+str(page)
      html=self.load(url,http)
      self.deal1(html,page)
      panduan = input("是否继续爬虫下一页(y/n)!")
      if panduan == "y":
        isflow = True
        page += 1
      else:
        isflow = False
  def load(self,url,http):
    '''
    针对url地址进行全部爬去
    :param url: url地址
    :return: 返回爬去的内容
    '''
    header = {
      "User-Agent": " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }
    #res = http.request('GET',url=url,fields={'wd':'iij'},headers=header)
    res = urllib.request.Request(url,headers=header)
    #print(res.status)
    #print(res.data.decode())
    resp = urllib.request.urlopen(res)
    html = resp.read().decode('utf-8')
    return html
  def deal1(self,html,page):
    '''
    对之前爬去的内容进行正则匹配，匹配职位所对应的链接a
    :param html:之前爬去的内容
    :param page: 正在爬去的页码
    '''
    parrten=re.compile('<a\s+style="font-weight:\s+bold"\s+par="ssidkey=y&amp;ss=\d+&amp;ff=\d+&amp;sg=\w+&amp;so=\d+"\s+href="(.*?)" rel="external nofollow" target="_blank">.*?</a>',re.S)
    til=parrten.findall(html)
    for t in til:
      self.deal2(t,page)
  def deal2(self,t,page):
    '''
    进行二次爬虫，然后在新的页面中对公司、薪资、工作经验进行匹配
    :param t: url地址
    :param page: 当前匹配的页数
    '''
    html=self.load(t)#返回二次爬虫的内容
    parrten1=re.compile('<a\s+onclick=".*?"\s+href=".*?" rel="external nofollow" \s+target="_blank">(.*?)\s+.*?<img\s+class=".*?"\s+src=".*?"\s+border="\d+"\s+vinfo=".*?"></a>',re.S)
    parrten2=re.compile('<li><span>职位月薪：</span><strong>(.*?)&nbsp;<a.*?>.*?</a></strong></li>',re.S)
    parrent3=re.compile('<li><span>工作经验：</span><strong>(.*?)</strong></li>',re.S)
    til1=parrten1.findall(html)
    til2=parrten2.findall(html)
    til3=parrent3.findall(html)
    str=""
    for t in til1:
      t=t.replace('<img title="专属页面" src="//img03.zhaopin.cn/2012/img/jobs/icon.png" border="0" />',"")
      str+=t
      str+="\t"
    for t in til2:
      str+=t
      str += "\t"
    for t in til3:
      str+=t
    self.writeData(str,page)
  def writeData(self,context,page):
    '''
    将最终爬去的内容写入文件中
    :param context: 匹配好的内容
     :param page: 当前爬去的页码数
    '''
    fileName = "di" + str(page) + "yehtml.txt"
    with open(fileName, "a") as file:
      file.writelines(context + "\n")
if __name__ == '__main__':
  position=input("请输入职位：")
  workPlace=input("请输入工作地点：")
  z=zhiLian()
  z.spider(position,workPlace)