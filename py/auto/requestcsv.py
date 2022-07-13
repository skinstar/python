import requests
from py.auto.readcsv import ReadCsv
r = ReadCsv()
ee = r.read_csv()
item = []
# print(ee)
class requestcsv():
    def requestscsv(self):
        item = []
        for csv_i in ee:
            if csv_i[2] =="get":
                rr = requests.get(csv_i[0],params=csv_i[1])
                item.append(rr.status_code)
            else:
                rr = requests.post(csv_i[0],data=csv_i[1])
                item.append(rr.status_code)
        return item

rr = requestcsv()
aaa = rr.requestscsv()
print(aaa)