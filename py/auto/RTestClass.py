from urllib.request import Request
import pytest
import os
import allure
from py.auto.requestcsv import requestcsv

r=requestcsv()
aa = r.requests_csv()
print(aa)
class TestClass():
    def test002(self):
        for i in aa:
            assert i ==200

if __name__ == '__main__':
    pytest.main(['--alluredir', 'report/result', 'test_02csv.py'])
    split = 'allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + '--clean'
    os.system(split)

