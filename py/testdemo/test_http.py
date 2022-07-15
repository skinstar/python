import os,sys                                     
urlp=os.path.join(os.getcwd(),"testdemo")
sys.path.append(urlp) 
print('test_http：路径系统：',sys.path)


import pytest
import allure
from auto.requestcsv import RequestCsv

r=RequestCsv()
aa = r.requests_csv()
print(aa)

def test_m2():
    print('测试')
    assert 1==1

class Test_class():
    def test_001(self):
        for i in aa:
            print('请求结果状态')
            assert i[1] ==200

if __name__ == '__main__':
    # pytest.main(['--alluredir', './report/result', 'test_http.py'])
    pytest.main(['./testdemo/test_http.py'])
    # 将测试报告转为html格式
    # split = 'allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + '--clean'
    # os.system(split)

