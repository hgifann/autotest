import src.utils.testjson1
import src.test.common.login
import json
import pytest
#输入正确的用户名和密码，登录成功；输入错误的登录名和密码登录失败

excelinfo=src.utils.testjson1.Read_excel().read_excel()


class Test_login:

    # def __init__(self,excelinfo):
    #     self.excelinfo=src.utils.testjson1.Read_excel().read_excel()
    #登录成功 ：输入正确的用户名和密码
    @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
    def test_login(self,url,service,username,password,is_allow_many,app_key):
        # print("username=====",username)
        # print("username=====",type(username))
        # if(len(username==0) or len(password ==0)):
        #     print("用户名或密码不能为空")
        # else:
        print("username====",username)
        print("password====",type(username))
        if(username.strip()=='' or password.strip()==''):
            print("用户名或密码不能为空")

            assert 0,"用户名或密码不能为空,登录失败"
        else:
            login=src.test.common.login.Login()

            # s=login.login(excelinfo['url'],excelinfo['service'],excelinfo['username'],excelinfo['password'],excelinfo['is_allow_many'],excelinfo['app_key'])
            s=login.login(url,service,username,password,is_allow_many,app_key)
            x=json.loads(s.text)

            print("respond is=====",x)

            err_code=x["data"]["err_code"]
            err_msg=x["data"]["err_msg"]
            if err_code==0:
                assert err_code  ==0
            # print(err_msg)

            else:

                assert err_code  !=0
            print(err_msg)
    # #登录失败测试，输入错误的用户名或者密码
    # @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
    # def test_login(self,url,service,username,password,is_allow_many,app_key):
    #
    #     login=src.test.common.login.Login()
    #     # s=login.login(excelinfo['url'],excelinfo['service'],excelinfo['username'],excelinfo['password'],excelinfo['is_allow_many'],excelinfo['app_key'])
    #     s=login.login(url,service,username,password,is_allow_many,app_key)
    #     x=json.loads(s.text)
    #     err_code=x["data"]["err_code"]
    #     assert err_code  ==1
    #
    #


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
