from email import header
import requests
from urllib import request
from urllib import parse

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

def get_json(url, num):
 """
 从指定的url中通过requests请求携带请求头和请求体获取网页中的信息,
 :return:
 """
 url1 = 'https://www.lagou.com/jobs/list_python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput='
 headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
  'Host': 'www.lagou.com',
  'Origin': 'https://www.lagou.com',
  'Referer': 'https://www.lagou.com/jobs/list_python%E5%BC%80%E5%8F%91%E5%B7%A5%E7%A8%8B%E5%B8%88?labelWords=&fromSearch=true&suginput=',
  'X-Anit-Forge-Code': '0',
  'X-Anit-Forge-Token': 'None',
  'X-Requested-With': 'XMLHttpRequest',
  'Cookie': 'JSESSIONID=C4FAB2F538B825F65893613ED73918EB'
 }
 data = {
  'first': 'true',
  'pn': num,
  'kd': 'python工程师'}
 content = request.Request(url,headers=headers,data=parse.urlencode(data).encode('utf-8'),method='POST')
 a = request.urlopen(content)
 print(a.read().decode('utf-8'))

 s = requests.Session()
 print('建立session：', s, '\n\n')
 s.get(url=url1, headers=headers, timeout=3)
 cookie = s.cookies
 print('获取cookie：', cookie, '\n\n')
 res = requests.post(url, headers=headers, data=data, cookies=cookie, timeout=3)
 res.raise_for_status()
 res.encoding = 'utf-8'
 page_data = res.json()
 print('请求响应结果：', page_data, '\n\n')
 return page_data
 
 
print(get_json(url, 1))