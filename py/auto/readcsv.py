# _*_ coding:utf-8 _*_
import csv

class ReadCsv():
    def read_csv(self):
        my_list = []
        fileD = open('D:\\data.csv',encoding='utf-8',errors='ignore')
        csv_con = csv.reader(fileD)
        for csv_in in csv_con:
            my_list.append(csv_in)
        my_list = my_list[1:]
        fileD.close()
        return my_list

cs = ReadCsv()
print('csv数据:',cs.read_csv())