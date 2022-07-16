#encoding=utf-8
import urllib
import urllib.request
import urllib.response
import chardet
import re


class teiba():
  def spider(self,name,startPage,endPage):
    url="http://tieba.baidu.com/f?ie=utf-8&"
    url+=urllib.parse.urlencode({"kw":name})
    for page in range(startPage,endPage+1):
      pn=50*(page-1)
      urlFull=url+"&"+urllib.parse.urlencode({"pn":pn})
      html=self.loadPage(url)
      self.dealPage(html,page)

  def loadPage(self,url):
    header={
      "User-Agent":" Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.79 Safari/537.36"
    }
    res = urllib.request.Request(url,headers=header)
    resp = urllib.request.urlopen(res)
    html=resp.read().decode('utf-8')
    return html
  def dealPage(self,html,page):
    partten=re.compile(r'<a\s+rel="noreferrer"\s+href="/p/\d+" rel="external nofollow" \s+title=".*?"\s+target="_blank" class="j_th_tit\s+">(.*?)</a>',re.S)
    titleList=partten.findall(html)
    rstr=r'<span\s+class="topic-tag"\s+data-name=".*?">#(.*?)#</span>'
    for title in titleList:
      title=re.sub(rstr,"",title)
      self.writePage(title,page)
  def writePage(self,context,page):
    fileName="di"+str(page)+"yehtml.txt"
    with open(fileName,"a") as file:
      file.writelines(context+"\n")
if __name__ == '__main__':
  name=input("请输入贴吧名：")
  startPage=input("请输入起始页：")
  endPage=input("请输入终止页：")
  t=teiba()
  t.spider(name,int(startPage),int(endPage))