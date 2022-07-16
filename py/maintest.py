import sys
import os
urlp=os.path.join(os.getcwd(),"testdemo")
sys.path.append(os.getcwd())
print('maintest路径系统：',sys.path)



import pytest

# 指定自定义的或额外的插件
class MyPlugin(object):
    def pytest_sessionfinish(self):
        print("*** test run reporting finishing")

if __name__ == '__main__':
    # pytest.main(['--alluredir', './report/result', 'maintest.py'])
    # pytest.main(["-qq"], plugins=[MyPlugin()])
    pytest.main(['--alluredir', './report/my_allure_result'])
    split = 'allure ' + 'generate ' + './report/my_allure_result ' + '-o ' + './report/html ' + '--clean'
    os.system(split)

