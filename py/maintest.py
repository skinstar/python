import sys
import os
urlp=os.path.join(os.getcwd(),"testdemo")
print('urlp',urlp)
sys.path.append(urlp)
sys.path.append('../root')
print('maintest路径系统：',sys.path)



import pytest

if __name__ == '__main__':
    # pytest.main(['--alluredir', './report/result', 'test_http.py'])
    pytest.main(['-k','test'])
 

