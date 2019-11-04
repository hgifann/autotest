__author__ = 'THTF'
import src.utils.testjson1
import src.test.common.register
import json
import pytest

#以class调用

excelinfo= src.utils.testjson1.Read_excel().read_excel()
class Test_register:
    @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
    def test_register(self,url,service,username,password,is_allow_many,app_key):

        reg=src.test.common.register.Register()
        s=reg.register(url,service,username,password,is_allow_many,app_key)
        x=json.loads(s.text)
        print("x======",x)
        returncode=x["ret"]
        if returncode==200:
            err_code=x["data"]["err_code"]
            err_msg=x["data"]["err_msg"]
            print("err_msg is====== ",err_msg)
            print("err_code is====== ",err_code)

            assert err_code  ==0
        else:
            msg=x["msg"]
            print("msg =====",msg)
            assert 1==0,"登录失败"


#以方法调用
# excelinfo= src.utils.testjson1.Read_excel().read_excel()
# @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
# def test_register(url,service,username,password,is_allow_many,app_key):
#
#     reg=src.test.common.register.Register()
#     s=reg.register(url,service,username,password,is_allow_many,app_key)
#     x=json.loads(s.text)
#     err_code=x["data"]["err_code"]
#     assert err_code  ==0
#
