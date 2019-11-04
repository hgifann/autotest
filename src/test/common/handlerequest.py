__author__ = 'THTF'



import requests
import json

class RunMethod:

	# requests 单独的 post 接口方法请求
    def post(self, url, params, header=None):
        res = None
        if header is not None:

            res = requests.post(url=url, params=params, headers=header).json()
        else:
            res = requests.post(url=url, params=params).json()
        return res

	# requests 单独的 get 接口方法请求
    def get(self, url, params=None, header=None):
        res = None
        if header is not None:
            res = requests.get(url=url, params=params, headers=header)
        else:
            print("params=====",params)
            res = requests.get(url=url, params=params)
        return res.json()

	# 根据请求方式，选择不同的请求方法
    def checkmethord(self, method, url, params=None, header=None):
        res = None
        if method == "post":
            print("params ====",params)

            res = self.post(url, params, header)
        else:
            print("params ====",params)
            res = self.get(url, params, header)
        return json.dumps(res, ensure_ascii=False, indent=4, sort_keys=True)


