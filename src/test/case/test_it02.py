import pytest
test_user_data = [{"user": "admin1", "psw": "111111"},
                  {"user": "admin1", "psw": "222222"}]

@pytest.fixture(scope="module")
def login(request):
    user = request.param["user"]
    psw = request.param["psw"]
    f4=3
    print("登录账户：%s" % user)
    print("登录密码：%s" % psw)
    if psw:
        return f4
    else:
        return f4+1

# indirect=True 声明login是个函数
@pytest.mark.parametrize("login", test_user_data, indirect=True)
def test_login(login):
    '''登录用例'''
    a = login
    print(login)
    print("测试用例中login的返回值:%s" % a)
    assert a, "失败原因：密码为空"