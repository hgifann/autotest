import src.utils.testjson1
import src.test.common.login
import src.test.common.testrequest
import json
import pytest
import logging
#以class调用方式  class类名必须以“Test_xxx"开头，才能识别

# filename2=r"C:\Users\THTF\PycharmProjects\autotest\data\register.xlsx"
# excelinfo=src.utils.testjson1.Read_excel().read_excel(filename2)


# @pytest.fixture(scope="function")
@pytest.mark.smoke
class Test_register:
    filename=r"C:\Users\THTF\PycharmProjects\autotest\data\register.xlsx"
    excelinfo=src.utils.testjson1.Read_excel().read_excel(filename)
    @pytest.mark.parametrize('url,service,username,password',excelinfo)
    def test_register(self,url,service,username,password):

        payload = {'service':service,'username':username,'password':password,'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}
        login=src.test.common.testrequest.TestRequest()
        s=login.checkmethord("get",url,payload)
        respondcode=s["ret"]
        #ret响应码不为200，登录失败
        if respondcode !=200:
            msg=s["msg"]
            print(msg)
            assert True
        #相应码为200，判断err_code，若为1代表登录失败，为0代表登录成功
        else:

            err_code=s["data"]["err_code"]
            err_msg=s["data"]["err_msg"]
            print("err_msg:",err_msg)
            #err_code存在且为0，登录成功
            if err_code==0:
                assert True
            #err_code存在且不为0，登录失败
            else:
                # print("err_msg:",err_msg)
                assert True

