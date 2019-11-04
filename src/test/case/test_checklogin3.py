import src.utils.testjson1
import src.test.common.checklogin
import src.test.common.login


#登录，并检查登录状态  ,获取每个登录的token，uuid
import pytest
import json


excelinfo=src.utils.testjson1.Read_excel().read_excel()
@pytest.fixture(params=excelinfo)
def test_login(request):
    ss=request.param
    login=src.test.common.login.Login()
    # s=login.login(url,service,username,password,is_allow_many,app_key)
    s=login.login(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5])
    x=json.loads(s.text)
    err_code=x["data"]["err_code"]
    uuid=x["data"]["uuid"]
    token=x["data"]["token"]
    usrinfo=(ss[0],ss[1],uuid,token,ss[5])
    print(usrinfo)
    return usrinfo

def test_checklogin(test_login):

    checkloginusr=src.test.common.checklogin.CheckLogin()
    checkinfo=checkloginusr.check_login(test_login[0],"App.User.Check",test_login[2],test_login[3],test_login[4])
    # checkinfo=checkloginusr.check_login(url,service,uuid,token,app_key)
    print("test_login[0]======",test_login[0])
    print("test_login[1]======",test_login[1])
    print("test_login[2]======",test_login[2])
    print("test_login[3]======",test_login[3])
    print("test_login[4]======",test_login[4])

    x=json.loads(checkinfo.text)
    print("x===========",x)


    err_code=x["data"]["err_code"]
    assert err_code==0

