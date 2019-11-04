__author__ = 'THTF'


import requests
import json


class Register():

    def register(self,url,service,username,password,is_allow_many,app_key):
        payload = {'service':'App.User.Register','username':username,'password':password,'is_allow_many':is_allow_many,"app_key":app_key}
        # print(payload)
        response = requests.get(url,params=payload)
        print(response.text)
        return response

        #
        # x=json.loads(response.text)
        # reginfo=x["data"]["err_code"]
        # # # print(type(reginfo))
        # return reginfo