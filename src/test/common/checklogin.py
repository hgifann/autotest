import requests
import json
#
# url='http://hn216.api.yesapi.cn/?'
# app_key='784DBD349CE644ABD3684A562C159585'
class CheckLogin:
    # def check_login(self,url,uuid,token,app_key,service="App.User.Check"):
    def check_login(self,url,service,uuid,token,app_key):
        payload = {'service':service,'uuid':uuid,'token':token,'app_key':app_key}
        # print(payload)
        response = requests.get(url,params=payload)
        print(response.text)
        return response
        # return response.status_code
        # print(response.status_code)
        # return response.status_code
        # x=json.loads(response.text)
        # err_code=x["data"]["err_code"]
        # # token=x["data"]["token"]
        # # uuid=x["data"]["uuid"]
        # # # print(token)
        # return err_code

# login(url,)



# CheckLogin.check_login()