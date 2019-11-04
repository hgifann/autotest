import requests
import json


class Login():

    def login(self,url,service,username,password,is_allow_many,app_key):
        # url="http://hn216.api.yesapi.cn/"
        payload = {'service':service,'username':username,'password':password,'is_allow_many':is_allow_many,'app_key':app_key}
        # payload = {'service':"App.User.Login",'username':"autotest15",'password':"174b086fc6358db6154bd951a8947837",'is_allow_many':"1",'app_key':"784DBD349CE644ABD3684A562C159585"}
        # print(payload)
        response = requests.get(url,params=payload)
        # print("=======")
        # print(response.text)
        return response

        # print(response.status_code)
        # # return response.status_code
        # x=json.loads(response.text)
        # err_code=x["data"]["err_code"]
        # err_msg=x["data"]["err_msg"]
        # uuid=x["data"]["uuid"]
        # token=x["data"]["token"]
        # print("uuid",uuid)
        # print("token",token)
        # print(err_msg)
        # token=x["data"]["token"]
        # uuid=x["data"]["uuid"]
        # # print(token)
        # return err_code,uuid,token





# a=Login().login("http://hn216.api.yesapi.cn/","App.User.Login","autotest15","174b086fc6358db6154bd951a8947837","1","784DBD349CE644ABD3684A562C159585")
# Login().login()