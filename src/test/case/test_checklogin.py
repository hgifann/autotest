import src.utils.testjson1
import src.test.common.checklogin
import src.test.common.login


#登录，并检查登录状态

import pytest
import json

excelinfo=src.utils.testjson1.Read_excel().read_excel()
@pytest.fixture(scope="function")
@pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
# @pytest.mark.parametrize('url,service,username,password,is_allow_many,app_key',excelinfo)
def test_login(url,service,username,password,is_allow_many,app_key):
    login=src.test.common.login.Login()
    s=login.login(url,service,username,password,is_allow_many,app_key)
    x=json.loads(s.text)
    err_code=x["data"]["err_code"]
    uuid=x["data"]["uuid"]
    token=x["data"]["token"]
    # assert err_code  ==0
    usrinfo=(url,service,uuid,token,app_key)
    # usrinfo.append(url)
    # print("usrinfo is",usrinfo)
    # print("-----------------")
    # print(usrinfo)
    # return url,service,uuid,token,app_key
    return usrinfo
# print("==========")
# @pytest.mark.parametrize('url,service,uuid,token,app_key',usrinfo)
@pytest.mark.parametrize("url,service,uuid,token,app_key",excelinfo)
def test_checklogin(url,service,uuid,token,app_key):
# def test_checklogin(usrinfo[0],usrinfo[1],usrinfo[2],usrinfo[3],usrinfo[4]):
# def test_checklogin(usrinfo[0],usrinfo[1],usrinfo[2],usrinfo[3],usrinfo[4]):
    checkloginusr=src.test.common.checklogin.CheckLogin()
    # checkinfo=checkloginusr.check_login(usrinfo[0],usrinfo[1],usrinfo[2],usrinfo[3],usrinfo[4])
    checkinfo=checkloginusr.check_login(url,service,uuid,token,app_key)
    x=json.loads(checkinfo.text)
    err_code=x["data"]["err_code"]
    assert err_code==0
#
#
#



