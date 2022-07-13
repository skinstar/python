import csv

class ReadCsv():
    def read_csv(self):
        my_list = []
        csv_con = csv.reader(open('D:\\data.csv'))
        for csv_in in csv_con:
            my_list.append(csv_in)
        my_list = my_list[1:]
        return my_list

cs = ReadCsv()
print(cs.read_csv())