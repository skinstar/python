import requests
import sys
from py.auto.readcsv import ReadCsv
r = ReadCsv()
ee = r.read_csv()
item = []
# print(ee)
class requestcsv():
    def requests_csv(self):
        item = []
        for csv_i in ee:
            url= []
            if csv_i[2] =="get":
                rr = requests.get(csv_i[0],params=csv_i[1])
                url.append(csv_i[0])
                url.append(rr.status_code)
            else:
                rr = requests.post(csv_i[0],data=csv_i[1])
                url.append(csv_i[0])
                url.append(rr.status_code)
            item.append(url)
        return item

rr = requestcsv()
res = rr.requests_csv()
print('请求结果:',res)