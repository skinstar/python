import requests
from lxml import etree

# 获取源码
html = requests.get("https://blog.csdn.net/it_xf?viewmode=contents")
print(html.text)
# 打印源码
etree_html = etree.HTML(html.text)
content = etree_html.xpath('//*[@id="mainBox"]/main/div[2]/div[1]/h4/a/text()')
for each in content:
    print(each)