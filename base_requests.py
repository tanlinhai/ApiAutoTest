#coding=utf-8
import requests
import json
from Read_main.read_config import handle_ini
import os
import sys
base_path = os.getcwd()
sys.path.append(base_path)

class BaseRequests:

    # 发送POST请求
    def sendPost(self, url, data, cookie=None, header=None):
        res = requests.post(url=url, data=data, cookies=cookie, headers=header).text
        return res
    # 发送GET请求
    def sendGet(self, url, data, cookie=None, header=None):
        res = requests.get(url=url, params=data, cookies=cookie, headers=header).text
        return res
    # 执行方法，传递method、URL、data参数
    def run_main(self, method, url, data, cookie=None, header=None):
        base_url = handle_ini.get_value('host')
        if 'http' not in url or 'https' not in url:
            url = base_url + url

        if method == 'GET':
            res = self.sendGet(url, data, cookie, header)
        else:
            res = self.sendPost(url, data, cookie, header)
        try:
            res = json.loads(res)
        except:
            print('这个结果是一个text')
        return res

request = BaseRequests()

if __name__ == "__main__":
    request = BaseRequests()
