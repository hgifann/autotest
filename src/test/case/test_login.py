import src.utils.testjson1
import src.test.common.login
import json
import pytest
import logging
#以class调用方式  class类名必须以“Test_xxx"开头，才能识别

excelinfo=src.utils.testjson1.Read_excel().read_excel()

logging.basicConfig(level=logging.DEBUG)

class Test_login:

    # def __init__(self,excelinfo):
    #     self.excelinfo=src.utils.testjson1.Read_excel().read_excel()

    @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
    def test_login(self,url,service,username,password,is_allow_many,app_key):

        login=src.test.common.login.Login()
        # s=login.login(excelinfo['url'],excelinfo['service'],excelinfo['username'],excelinfo['password'],excelinfo['is_allow_many'],excelinfo['app_key'])
        s=login.login(url,service,username,password,is_allow_many,app_key)
        x=json.loads(s.text)
        err_code=x["data"]["err_code"]
        assert err_code  ==0


#以方法调用方式
# excelinfo=src.utils.testjson1.Read_excel().read_excel()
#
# @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
# def test_login(url,service,username,password,is_allow_many,app_key):
#
#     login=src.test.common.login.Login()
#     # s=login.login(excelinfo['url'],excelinfo['service'],excelinfo['username'],excelinfo['password'],excelinfo['is_allow_many'],excelinfo['app_key'])
#     s=login.login(url,service,username,password,is_allow_many,app_key)
#     x=json.loads(s.text)
#     err_code=x["data"]["err_code"]
#     assert err_code  ==0
