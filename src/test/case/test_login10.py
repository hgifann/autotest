import src.utils.testjson1
import src.test.common.login
import src.test.common.testrequest
import json
import pytest
import logging
#以class调用方式  class类名必须以“Test_xxx"开头，才能识别

filename=r"C:\Users\THTF\PycharmProjects\autotest\data\login.xlsx"
excelinfo=src.utils.testjson1.Read_excel().read_excel(filename)

class Test_login:
    @pytest.mark.parametrize('url,service,username,password',excelinfo)
    def test_login(self,url,service,username,password):

        payload = {'service':service,'username':username,'password':password,'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}


        login=src.test.common.testrequest.TestRequest()
        s=login.checkmethord("get",url,payload)
        err_code=s["data"]["err_code"]
        assert err_code   ==0
