# _*_ coding:utf-8 _*_
import os,sys                                     
urlp=os.path.join(os.getcwd(),"py")
sys.path.append(os.getcwd()) 
print('test_http：路径系统：',sys.path)


import pytest
import allure
from auto.requestcsv import RequestCsv

r=RequestCsv()
aa = r.requests_csv()
print(aa)

@allure.step("步骤1：打印")
def test_m2():
    print('测试')
    assert 1==1

@allure.feature("搜索")
class Test_class():
    @allure.story("百度搜索")
    def test_1(self):
        for i in aa:
            print('请求结果状态')
            assert i[1] ==200,'请求成功'
    @allure.story("谷歌搜索")
    def test_2(self):
        '''这是测试谷歌搜索'''
        assert 1 == 2, "搜索失败"

if __name__ == '__main__':
    # 生成报告 json
    pytest.main(['--alluredir', './report/my_allure_result', 'test_http.py'])
    # pytest.main()
    # 将测试报告转为html格式
    split = 'allure ' + 'generate ' + './report/my_allure_result ' + '-o ' + './report/html ' + '--clean'
    os.system(split)

    #也可用命令生成  pytest --html=./yxw/report.html

