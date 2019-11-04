__author__ = 'THTF'
import src.utils.testjson1



#注册  登录
import pytest
import json
import src.test.common.testrequest
filename=r"C:\Users\THTF\PycharmProjects\autotest\data\registerandlogin.xlsx"
excelinfo=src.utils.testjson1.Read_excel().read_excel(filename)

# =======================
@pytest.fixture(params=excelinfo)
def test_register(request):
    ss=request.param
    url=ss[0]
    register_service=ss[1]
    login_service=ss[2]
    username=ss[3]
    password=ss[4]
    payload = {'service':ss[1],'username':ss[3],'password':ss[4],'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}
    login=src.test.common.testrequest.TestRequest()
    s=login.checkmethord("get",ss[0],payload)
    err_code=s["data"]["err_code"]
    # uuid=s["data"]["uuid"]
    # token=s["data"]["token"]
    print("s=======",s)
    assert err_code  ==0
    return url,login_service,username,password

def test_checklogin(test_register):
    print("test===========",test_register)
    # uuid=test_register[0]
    # token=test_register[1]
    url=test_register[0]
    login_service=test_register[1]
    username=test_register[2]
    password=test_register[3]
    payload = {'service':login_service,'username':username,'password':password,'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}
    login=src.test.common.testrequest.TestRequest()
    s=login.checkmethord("get",url,payload)
    err_code=s["data"]["err_code"]
    assert err_code   ==0
# # =================

# 8个用例
# @pytest.mark.parametrize('url,register_service,login_service,username,password',excelinfo)
#
# class Test_registerandlogin:
#     # @pytest.mark.parametrize('url,register_service,login_service,username,password',excelinfo)
#     def test_register(self,url,register_service,login_service,username,password):
#         # ss=request.param
#         # url=ss[0]
#         # register_service=ss[1]
#         # login_service=ss[2]
#         # username=ss[3]
#         # password=ss[4]
#         payload = {'service':register_service,'username':username,'password':password,'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}
#         login=src.test.common.testrequest.TestRequest()
#         s=login.checkmethord("get",url,payload)
#         err_code=s["data"]["err_code"]
#         # uuid=s["data"]["uuid"]
#         # token=s["data"]["token"]
#         print("s=======",s)
#         assert err_code  ==0
#         return url,login_service,username,password
#     # @pytest.mark.parametrize('url,register_service,login_service,username,password',excelinfo)
#     def test_checklogin(self,url,register_service,login_service,username,password):
#         # uuid=test_register[0]
#         # token=test_register[1]
#         # url=test_register[0]
#         # login_service=test_register[1]
#         # username=test_register[2]
#         # password=test_register[3]
#         payload = {'service':login_service,'username':username,'password':password,'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}
#         login=src.test.common.testrequest.TestRequest()
#         s=login.checkmethord("get",url,payload)
#         err_code=s["data"]["err_code"]
#         assert err_code   ==0
#
