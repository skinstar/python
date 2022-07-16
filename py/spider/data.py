import re
import time

str = "fChina is a great country"
x = re.findall(".*a", str)
print(x)

with open(r'D:\文本.txt',mode='at',encoding='utf-8') as f:
    f.write(f'时间：{time.strftime("%Y-%m-%d %H:%M:%S")}，操作打开')

