__author__ = 'THTF'
import pytest
class Test_runpytest:
    if __name__ == '__main__':
        #执行一组用例，在此路径下，标签为logintest
        pytest.main(["-s",r"C:\Users\THTF\PycharmProjects\autotest\src\test\case","-m=logintest"])
        # pytest.main(["-s",r"C:\Users\THTF\PycharmProjects\autotest\src\test\suite"])
        # pytest.main(["-s",r"C:\Users\THTF\PycharmProjects\autotest\src\test\suite\test_login10.py",r"C:\Users\THTF\PycharmProjects\autotest\src\test\suite\test_login101.py"])
        # pytest.main(["-s",r"C:\Users\THTF\PycharmProjects\autotest\src\test\case\test_login10.py",r"C:\Users\THTF\PycharmProjects\autotest\src\test\case\test_register10.py"])
