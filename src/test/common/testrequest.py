__author__ = 'THTF'
import requests
import json

class TestRequest():

    def __init__(self):

        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"}

    def get(self, url, params):

        # try:
            r = requests.get(url=url, params=params, headers=self.headers)
            response = json.loads(r.text)
            print("get请求结果为：%s"%response)
            return response

        # except BaseException as e:
        #     print("get请求错误，错误原因：%s"%e)

    def post(self, url, params):

        data = json.dumps(params)
        # try:
        r = requests.post(url=url, json=data, headers=self.headers)
        response = json.loads(r.text)
        print("post请求结果为：%s" %response)
        return response

        # except BaseException as e:
        #     print("post请求错误，错误原因：%s" % e)

    def checkmethord(self,method,url,params,header=None):
        if method == "post":
            print("params 1====",params)

            res = self.post(url, params)
        else:
            print("params2 ====",params)
            res = self.get(url, params)
        return res


